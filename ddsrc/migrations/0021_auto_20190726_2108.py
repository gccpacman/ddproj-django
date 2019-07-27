# Generated by Django 2.2.1 on 2019-07-26 13:08

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0020_auto_20190726_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='polylines_bmap',
            field=django_mysql.models.JSONField(default=dict, null=True, verbose_name='坐标点(百度地图)'),
        ),
        migrations.AddField(
            model_name='road',
            name='polylines_gaode',
            field=django_mysql.models.JSONField(default=dict, null=True, verbose_name='坐标点(高德地图)'),
        ),
    ]