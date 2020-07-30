from ddsrc.models import Architecture
from django.db import models

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class TravelPath(models.Model):
    class Meta:
        verbose_name = '路线'
        verbose_name_plural = '路线'

    _id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="路线名称", max_length=128, blank=False)
    image = models.ImageField(upload_to='pic/travelpath/', null=True, blank=True)
    method = models.CharField(verbose_name="交通工具", max_length=128, blank=False)
    duration = models.CharField(verbose_name="游览时长", max_length=128, blank=False)
    feature = models.CharField(verbose_name="路线特色", max_length=128, blank=False)
    longitude = models.FloatField(verbose_name="经度", null=True, default=0.0)
    latitude = models.FloatField(verbose_name="纬度", null=True, default=0.0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    @property
    def path_points(self):
        travel_path_points = TravelPathPoint.objects.filter(travel_path=self).order_by('-priority')
        pathList = []
        for travel_path_point in travel_path_points:
            pathList.append({
                '_id': travel_path_point._id, 
                'name': travel_path_point.name,
                'distance': travel_path_point.distance,
                'duration': travel_path_point.duration,
                'highlight': travel_path_point.highlight,
                'is_cinema': travel_path_point.is_cinema,
                'architecture_id': travel_path_point.architecture_id,
                'address': travel_path_point.address,
                'priority': travel_path_point.priority,
                'longitude': travel_path_point.longitude,
                'latitude': travel_path_point.latitude,
                'image': travel_path_point.image.url if travel_path_point.image else '',
            })
        return pathList


class TravelPathPoint(models.Model):
    class Meta:
        verbose_name = '路线点'
        verbose_name_plural = '路线点'

    _id = models.AutoField(primary_key=True)
    travel_path = models.ForeignKey("TravelPath", on_delete=models.CASCADE)
    priority = models.IntegerField(verbose_name='排序', default=0)
    name = models.CharField(verbose_name="路线点名称", max_length=128, blank=False)
    distance = models.CharField(verbose_name="距离", max_length=128, blank=False)
    architecture_id = models.IntegerField(verbose_name='建筑id', blank=True, default=0)
    address = models.CharField(max_length=256, verbose_name="地址", null=True, blank=True)
    longitude = models.FloatField(verbose_name="经度", null=True, default=0.0)
    latitude = models.FloatField(verbose_name="纬度", null=True, default=0.0)
    image = models.ImageField(upload_to='pic/travelpathpoint/', null=True, blank=True)
    duration = models.CharField(verbose_name="浏览时间", max_length=128, blank=False)
    highlight = models.CharField(verbose_name="亮点", max_length=128, blank=False)
    is_cinema = models.BooleanField(verbose_name="是否是影院", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class RichTextArticle(models.Model):
    class Meta:
        verbose_name = '图文内容'
        verbose_name_plural = '图文内容'

    _id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="文章名称", max_length=128, blank=False)
    image = models.ImageField(upload_to='pic/richtext/', null=True, blank=True)
    body = RichTextUploadingField(verbose_name="文章内容",)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
