from django.db import models

class Movie(models.Model):

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name="中文名", unique=False, db_index=True)
    pub_time = models.CharField(max_length=32, verbose_name="发布时间")
    type = models.CharField(max_length=32, verbose_name="类型")