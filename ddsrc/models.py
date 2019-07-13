from django.db import models


class Road(models.Model):
    name_chs = models.CharField(max_length=64, verbose_name="现路名")
    name_en = models.CharField(max_length=64, verbose_name="英文名")
    temporal_value = models.CharField(max_length=64, verbose_name="开始/结束时间")
    history_of_name =  models.CharField(max_length=64, verbose_name="历史路名")
    name_after = models.CharField(max_length=64, verbose_name="")
    uri = models.URLField(verbose_name="")
    history_of = models.URLField(verbose_name="")
    des = models.TextField(verbose_name="简介(上海图书馆数据)")
    des2 = models.TextField(verbose_name="简介(手动编辑)")
    place_uri = models.URLField(verbose_name="所在区URI")
    place_name = models.CharField(max_length=64, verbose_name="所在区")
    is_from_lib = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Architecture(models.Model):
    road = models.ForeignKey("Road", on_delete=models.SET_NULL, null=True)
    name_cht = models.CharField(max_length=64, verbose_name="繁体名")
    name_chs = models.CharField(max_length=64, verbose_name="简体名")
    name_en = models.CharField(max_length=64, verbose_name="英文名")
    houseNumber = models.CharField(max_length=16, verbose_name="")
    address = models.CharField(max_length=256, verbose_name="地址")
    longitude = models.FloatField(verbose_name="经度")
    latitude = models.FloatField(verbose_name="纬度")
    place_uri = models.URLField(verbose_name="所在区URI")
    place_name = models.CharField(max_length=64, verbose_name="所在区")
    des = models.TextField(verbose_name="简介(上海图书馆数据)")
    des2 = models.TextField(verbose_name="简介(手动编辑)")
    first_image_uri = models.URLField(verbose_name="首页照片URI", null=True)
    first_image_path = models.ImageField(upload_to='pic/architecture_first/',null=True)
    batch_no = models.CharField(max_length=16, verbose_name="批次")
    protect_type = models.CharField(max_length=16, verbose_name="保护类型")
    is_from_lib = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ArchitecturePicture(models.Model):
    architecture = models.ForeignKey("Architecture", on_delete=models.CASCADE)
    pic_uri= models.URLField()
    pic_format = models.CharField(max_length=16)
    pic_file = models.ImageField(upload_to='pic/architecture/',null=True)
    des = models.TextField(verbose_name="简介(上海图书馆数据)")
    des2 = models.TextField(verbose_name="简介(手动编辑)")
    is_from_lib = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
