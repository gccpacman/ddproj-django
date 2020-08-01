from django.db import models

class Peotry(models.Model):

    class Meta:
        verbose_name = '对诗'
        verbose_name_plural = '对诗'

    _id = models.AutoField(primary_key=True)
    firstWord = models.CharField(max_length=64, verbose_name="输入", null=False, unique=True)
    result = models.CharField(max_length=256, verbose_name="输出", null=True, blank=True, default='')
    status = models.IntegerField(default=0)
    taskId = models.CharField(max_length=256, verbose_name="taskId", default='')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

class PeotryBackground(models.Model):

    class Meta:
        verbose_name = '背景图片'
        verbose_name_plural = '背景图片'

    _id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name="背景图片", upload_to='movie/peoples/', null=True, blank=True)
    qr_image = models.ImageField(verbose_name="二维码图片", upload_to='movie/peoples/', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")