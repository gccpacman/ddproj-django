from django.db import models
from django_mysql.models import JSONField


class Movie(models.Model):

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    name = models.CharField(max_length=64, verbose_name="电影名", unique=False, db_index=True)
    pub_date = models.CharField(max_length=32, verbose_name="发布时间", default="")
    movie_type = models.CharField(max_length=128, verbose_name="类型", default="")
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
        verbose_name = '电影照片'
        verbose_name_plural = '电影照片'

    _id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=128, verbose_name="URI", unique=True)
    raw = JSONField(verbose_name="元数据", null=True)
    photoType = models.CharField(max_length=64, null=True, default=None)
    movieName = models.CharField(max_length=128, verbose_name="电影名称",null=True)
    movieUri = models.CharField(max_length=128, verbose_name="电影URI",null=True)
    photo_date = models.DateField(verbose_name="日期", null=True)
    image = models.ImageField(verbose_name="图片", upload_to='movie/photos/', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class MoviePhotoRelation(models.Model):

    class Meta:
        verbose_name = '照片关系'
        verbose_name_plural = '照片关系'

    _id = models.AutoField(primary_key=True)
    photoUri = models.CharField(max_length=128, verbose_name="剧照URI", null=False)
    relationUri = models.CharField(max_length=128, verbose_name="关系URI", null=False)
    relationName = models.CharField(max_length=128, verbose_name="关系名称", null=True)
    relationType = models.CharField(max_length=32, verbose_name="关系类型", null=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
