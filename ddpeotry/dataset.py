# -*- coding: utf-8 -*-
# @File    : dataset.py
# @Author  : AaronJny
# @Time    : 2019/12/24
# @Desc    : 构建数据集
import tensorflow as tf
from collections import defaultdict
from bert4keras.tokenizers import Tokenizer, load_vocab
from bert4keras.snippets import sequence_padding, DataGenerator
from bert4keras.models import build_transformer_model

import numpy as np
from ddproj import settings



class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PeotryTokenizer(metaclass=Singleton):

    keep_words = []
    tokenizer = None
    model= None

    def __init__(self):

        # 预训练模型参数
        config_path = settings.CONFIG_PATH
        checkpoint_path = settings.CHECKPOINT_PATH
        dict_path = settings.DICT_PATH

        # 禁用词
        disallowed_words = settings.DISALLOWED_WORDS
        # 句子最大长度
        max_len = settings.MAX_LEN
        # 最小词频
        min_word_frequency = settings.MIN_WORD_FREQUENCY
        # mini batch 大小
        batch_size = settings.BATCH_SIZE

        # 加载数据集
        with open(settings.DATASET_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 将冒号统一成相同格式
            lines = [line.replace('：', ':') for line in lines]
            
        # 数据集列表
        poetry = []
        # 逐行处理读取到的数据
        for line in lines:
            # 有且只能有一个冒号用来分割标题
            if line.count(':') != 1:
                continue
            # 后半部分不能包含禁止词
            __, last_part = line.split(':')
            ignore_flag = False
            for dis_word in disallowed_words:
                if dis_word in last_part:
                    ignore_flag = True
                    break
            if ignore_flag:
                continue
            # 长度不能超过最大长度
            if len(last_part) > max_len - 2:
                continue
            poetry.append(last_part)

        # 预训练模型中的词典和分词器
        _token_dict = load_vocab(dict_path)
        _tokenizer = Tokenizer(dict_path, do_lower_case=True)

        # 统计所有词的词频
        word_frequency_count = defaultdict(int)
        for line in poetry:
            for t in _tokenizer.tokenize(line):
                word_frequency_count[t] += 1
        # 过滤掉低频词
        tokens = [(token, count) for token, count in word_frequency_count.items() if count >= min_word_frequency]
        # 按词频排序
        tokens = sorted(tokens, key=lambda x: -x[1])
        # 去掉词频，只保留词列表
        tokens = [token for token, count in tokens]

        # 构建新的token->id映射关系、和新词表
        token_id_dict = {}

        # 将特殊词加入到词典中
        for token in ['[PAD]', '[UNK]', '[CLS]', '[SEP]']:
            token_id_dict[token] = len(token_id_dict)
            self.keep_words.append(_token_dict[token])
        # 将唐诗数据集中的词加入到词典中
        for token in tokens:
            # 在bert的词典里，但还没有被加载到新词典里的词，才会被加入
            if token in _token_dict and token not in token_id_dict:
                token_id_dict[token] = len(token_id_dict)
                self.keep_words.append(_token_dict[token])

        # 使用新词典重新建立分词器
        self.tokenizer = Tokenizer(token_id_dict, do_lower_case=True)
        # 混洗数据
        np.random.shuffle(poetry)
        self.model = self.get_model()
        self.model.load_weights(settings.BEST_MODEL_PATH)


    def get_model(self):

        model = build_transformer_model(
            settings.CONFIG_PATH, 
            settings.CHECKPOINT_PATH, 
            application='lm', 
            keep_tokens=keep_words
        )
        model.summary()

        # loss fun，交叉熵
        # 输入的数据，从第二个字符开始，可以作为正确的目标结果(输入是没有经过one-hot编码的)
        y_true = model.input[0][:, 1:]
        # 目标mask
        y_mask = model.get_layer('Embedding-Token').output_mask[:, 1:]
        y_mask = tf.cast(y_mask, tf.float32)
        # 预测结果，到倒数第二个（包括）时结束
        y_pred = model.output[:, :-1]
        cross_entropy = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
        cross_entropy = tf.reduce_sum(cross_entropy * y_mask) / tf.reduce_sum(y_mask)
        model.add_loss(cross_entropy)
        model.compile(tf.keras.optimizers.Adam(1e-5))

        return model

    def generate_random_poetry(self, s=''):
        """
        随机生成一首诗
        :param tokenizer: 分词器
        :param model: 用于生成古诗的模型
        :param s: 用于生成古诗的起始字符串，默认为空串
        :return: 一个字符串，表示一首古诗
        """
        tokenizer = self.tokenizer
        model = self.model

        # 将初始字符串转成token
        token_ids, segment_ids = tokenizer.encode(s)
        # 去掉结束标记[SEP]
        token_ids = token_ids[:-1]
        # 去掉对应的segment
        segment_ids = segment_ids[:-1]
        # 保存所有预测出的id的列表
        target_ids = []
        while len(token_ids) + len(target_ids) < settings.MAX_LEN:
            # 将给定的初始token和预测出的token扩展到一起，作为输入
            _target_ids = token_ids + target_ids
            _segment_ids = segment_ids + [0 for _ in target_ids]
            # 进行预测，只保留第一个样例（我们输入的样例数只有1）的、最后一个token的预测的、不包含[PAD][UNK][CLS]的概率分布
            _probas = model.predict([[_target_ids, ], [_segment_ids, ]])[0, -1, 3:]
            # 此时_probas的shape为(3188,)，其中3188是我们当前数据下的词汇表大小-3
            # print(_probas.shape)
            # 按照出现概率，对所有token倒序排列
            p_args = _probas.argsort()[::-1][:100]
            # 排列后的概率顺序
            p = _probas[p_args]
            # 先对概率归一
            p = p / sum(p)
            # 再按照预测出的概率，随机选择一个词作为预测结果
            target_index = np.random.choice(len(p), p=p)
            target = p_args[target_index] + 3
            # 保存
            target_ids.append(target)
            if target == 3:
                break
        return tokenizer.decode(token_ids + target_ids)


    def generate_acrostic(self, head):
        """
        随机生成一首藏头诗
        :param tokenizer: 分词器
        :param model: 用于生成古诗的模型
        :param head: 藏头诗的头
        :return: 一个字符串，表示一首古诗
        """
        tokenizer = self.tokenizer
        model = self.model
        # 使用空串初始化token_ids，加入[CLS]
        token_ids, segment_ids = tokenizer.encode('')
        token_ids = token_ids[:-1]
        segment_ids = segment_ids[:-1]
        # 标点符号，这里简单的只把逗号和句号作为标点
        punctuations = ['，', '。']
        punctuation_ids = {tokenizer.token_to_id(token) for token in punctuations}
        # 缓存生成的诗的list
        poetry = []
        # 对于藏头诗中的每一个字，都生成一个短句
        for ch in head:
            # 先记录下这个字
            poetry.append(ch)
            # 将藏头诗的字符转成token id
            token_id = tokenizer.token_to_id(ch)
            # 加入到列表中去
            token_ids.append(token_id)
            segment_ids.append(0)
            # 开始生成一个短句
            while True:
                # 进行预测，只保留第一个样例（我们输入的样例数只有1）的、最后一个token的预测的、不包含[PAD][UNK][CLS]的概率分布
                _probas = model.predict([[token_ids, ], [segment_ids, ]])[0, -1, 3:]
                # 按照出现概率，对所有token倒序排列
                p_args = _probas.argsort()[::-1][:100]
                # 排列后的概率顺序
                p = _probas[p_args]
                # 先对概率归一
                p = p / sum(p)
                # 再按照预测出的概率，随机选择一个词作为预测结果
                target_index = np.random.choice(len(p), p=p)
                target = p_args[target_index] + 3
                # 保存
                token_ids.append(target)
                segment_ids.append(0)
                # 只有不是特殊字符时，才保存到poetry里面去
                if target > 3:
                    poetry.append(tokenizer.id_to_token(target))
                if target in punctuation_ids:
                    break
        return ''.join(poetry)
