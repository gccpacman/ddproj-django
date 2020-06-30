from django.db import models


# class GeneralCache(models.Model):

#     class Meta:
#         verbose_name = '通用缓存'
#         verbose_name_plural = '通用缓存'

#     _id = models.AutoField(primary_key=True)
#     obj_type = models.CharField(
#         max_length=32, verbose_name="类型")
#     obj_uri = models.CharField(
#         max_length=128, verbose_name="URI"
#     )
#     raw = JSONField(verbose_name="元数据", null=True)
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")