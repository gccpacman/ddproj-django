from django.db import models


class Road(models.Model):
    class Meta:
        verbose_name = '马路'
        verbose_name_plural = '马路'

    _id = models.AutoField(primary_key=True)
    name_chs = models.CharField(max_length=64, verbose_name="现路名", unique=True)
    name_en = models.CharField(max_length=64, verbose_name="英文名", null=True)
    temporal_value = models.CharField(max_length=64, verbose_name="开始/结束时间", null=True)
    name_after = models.CharField(max_length=64, verbose_name="以..命名", null=True)
    history_of_name =  models.CharField(max_length=64, verbose_name="历史", null=True)
    history_of_lib_uri = models.URLField(verbose_name="历史关联URI", null=True)
    des = models.TextField(verbose_name="简介(上海图书馆数据)", null=True)
    des2 = models.TextField(verbose_name="简介(手动编辑)", null=True)
    place_uri = models.URLField(verbose_name="所在区URI", null=True)
    place_name = models.CharField(max_length=64, verbose_name="所在区", null=True)
    is_from_lib = models.BooleanField(default=True)
    lib_uri = models.URLField(verbose_name="URI", null=True)
    lib_update_time= models.DateTimeField(null=True, verbose_name="数据获取时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return 'Road: ' + self.name_chs


class Architecture(models.Model):
    class Meta:
        verbose_name = '建筑'
        verbose_name_plural = '建筑'

    _id = models.AutoField(primary_key=True)
    road = models.ForeignKey("Road", on_delete=models.SET_NULL, null=True)
    road_name_chs = models.CharField(max_length=64, verbose_name="马路简体名", null=True)
    road_lib_uri = models.URLField(verbose_name="马路URI", null=True)
    name_chs = models.CharField(max_length=64, verbose_name="简体名", unique=True, null=True)
    name_cht = models.CharField(max_length=64, verbose_name="繁体名", null=True)
    name_en = models.CharField(max_length=128, verbose_name="英文名", null=True)
    house_number = models.CharField(max_length=256, verbose_name="房间号", null=True)
    address = models.CharField(max_length=256, verbose_name="地址", null=True)
    longitude = models.FloatField(verbose_name="经度", null=True)
    latitude = models.FloatField(verbose_name="纬度", null=True)
    place_uri = models.URLField(verbose_name="所在区URI", null=True)
    place_name = models.CharField(max_length=64, verbose_name="所在区", null=True)
    des = models.TextField(verbose_name="简介(上海图书馆数据)", null=True)
    des2 = models.TextField(verbose_name="简介(手动编辑)", null=True, blank=True)
    first_image_lib_uri = models.URLField(verbose_name="首页照片图书馆URI", null=True)
    first_image_uri = models.URLField(verbose_name="首页照片网址", null=True)
    first_image_path = models.ImageField(upload_to='pic/architecture_first/',null=True)
    batch_no = models.CharField(max_length=16, verbose_name="批次", null=True)
    protect_type = models.CharField(max_length=128, verbose_name="保护类型", null=True)
    is_from_lib = models.BooleanField(default=True)
    lib_is_red = models.IntegerField(default=3)
    lib_uri = models.URLField(verbose_name="URI", null=True)
    lib_update_time= models.DateTimeField(null=True, verbose_name="数据获取时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return 'Architecture: ' + self.name_chs

    def road_str(self):
        if self.road:
            return str(road)

class ArchitecturePicture(models.Model):
    class Meta:
        verbose_name = '优秀历史建筑图片'
        verbose_name_plural = '优秀历史建筑图片'

    _id = models.AutoField(primary_key=True)
    architecture = models.ForeignKey("Architecture", on_delete=models.CASCADE)
    pic_uri= models.URLField(null=True)
    pic_format = models.CharField(max_length=16, null=True, blank=True)
    pic_file = models.ImageField(upload_to='pic/architecture/',null=True)
    des = models.TextField(verbose_name="简介(上海图书馆数据)", null=True, blank=True)
    des2 = models.TextField(verbose_name="简介(手动编辑)", null=True, blank=True)
    is_from_lib = models.BooleanField(default=True)
    lib_uri = models.URLField(verbose_name="URI", null=True)
    lib_update_time= models.DateTimeField(null=True, verbose_name="数据获取时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
