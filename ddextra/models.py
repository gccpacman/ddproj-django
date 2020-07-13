from django.db import models


class TravelPath(models.Model):
    class Meta:
        verbose_name = '路线'
        verbose_name_plural = '路线'

    _id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="路线名称", max_length=128, blank=False)
    method = models.CharField(verbose_name="交通工具", max_length=128, blank=False)
    duration = models.CharField(verbose_name="游览时长", max_length=128, blank=False)
    feature = models.CharField(verbose_name="路线特色", max_length=128, blank=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class TravelPathPoint(models.Model):
    class Meta:
        verbose_name = '路线点'
        verbose_name_plural = '路线点'

    _id = models.AutoField(primary_key=True)
    travel_path = models.ForeignKey("TravelPath", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="路线点名称", max_length=128, blank=False)
    distance = models.CharField(verbose_name="距离", max_length=128, blank=False)
    duration = models.CharField(verbose_name="浏览时间", max_length=128, blank=False)
    highlight = models.CharField(verbose_name="亮点", max_length=128, blank=False)
    is_cinema = models.BooleanField(verbose_name="是否是影院", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")