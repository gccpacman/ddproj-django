from django.db import models

class Peotry(models.Model):

    class Meta:
        verbose_name = '电影照片'
        verbose_name_plural = '电影照片'

    _id = models.AutoField(primary_key=True)
    firstWord = models.CharField(max_length=64, verbose_name="输入", null=True, default=None)
    result = models.CharField(max_length=256, verbose_name="输出", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")