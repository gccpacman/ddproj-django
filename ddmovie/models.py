from django.db import models
from django_mysql.models import JSONField


class Movie(models.Model):

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="中文名", unique=False, db_index=True)
    pub_date = models.CharField(max_length=32, verbose_name="发布时间", default="")
    movie_type = models.CharField(max_length=32, verbose_name="类型", default="")
    raw = JSONField(verbose_name="元数据", null=True)
    detail_raw = JSONField(verbose_name="详细信息元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class MoviePeople(models.Model):

    class Meta:
        verbose_name = '艺人'
        verbose_name_plural = '艺人'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="姓名", unique=False, db_index=True)
    speciality = models.CharField(max_length=128, verbose_name="职业", default="")
    nationality = models.CharField(max_length=128, verbose_name="国籍", default="")
    raw = JSONField(verbose_name="元数据", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class MoviePhoto(models.Model):

    class Meta:
        verbose_name = '剧照'
        verbose_name_plural = '剧照'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    raw = JSONField(verbose_name="元数据", null=True)
    filePath = models.ImageField(verbose_name="图片地址", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")