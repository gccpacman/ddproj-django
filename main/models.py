from django.db import models


class Road(models.Model):
    name_chs = models.CharField(max_length=64, description="现路名")
    name_en = models.CharField(max_length=64, description="英文名")
    temporal_value = models.CharField(max_length=64, description="开始/结束时间")
    history_of_name =  models.CharField(max_length=64, description="历史路名")
    name_after = models.CharField(max_length=64, description="")
    uri = models.URLField(description="")
    history_of = models.URLField(description="")
    description = models.TextField(description="简介")
    place_uri = models.URLField(description="所在区URI")
    place_name = models.CharField(description="所在区")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Architecture(models.Model):
    name_cht = models.CharField(max_length=64, description="繁体名")
    name_chs = models.CharField(max_length=64, description="简体名")
    name_en = models.CharField(max_length=64, description="英文名")
    houseNumber = models.CharField(max_length=16, description="")
    address = models.CharField(max_length=256, description="地址")
    longitude = models.FloatField(description="经度")
    latitude = models.FloatField(description="纬度")
    place_uri = models.URLField(description="所在区URI")
    place_name = models.CharField(description="所在区")
    des = models.TextField(description="简介(上海图书馆数据)")
    description = models.TextField(description="简介")
    batch_no = models.CharField(max_length=16, description="批次")
    protect_type = models.CharField(max_length=16, description="保护类型")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
