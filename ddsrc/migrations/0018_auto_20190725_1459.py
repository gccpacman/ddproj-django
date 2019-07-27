# Generated by Django 2.2.1 on 2019-07-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0017_auto_20190725_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='des2',
            field=models.TextField(blank=True, null=True, verbose_name='简介(手动编辑)'),
        ),
        migrations.AlterField(
            model_name='road',
            name='place_name2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='所在区(手动编辑)'),
        ),
        migrations.AlterField(
            model_name='road',
            name='related_place',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='关联地名'),
        ),
        migrations.AlterField(
            model_name='road',
            name='related_place_province',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='关联地省份'),
        ),
    ]