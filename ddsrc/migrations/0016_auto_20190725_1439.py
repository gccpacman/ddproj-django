# Generated by Django 2.2.1 on 2019-07-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0015_auto_20190725_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='place_name2',
            field=models.CharField(max_length=64, null=True, verbose_name='所在区'),
        ),
        migrations.AddField(
            model_name='road',
            name='related_place',
            field=models.CharField(max_length=128, null=True, verbose_name='关联地名'),
        ),
        migrations.AddField(
            model_name='road',
            name='related_place_province',
            field=models.CharField(max_length=64, null=True, verbose_name='关联地省份'),
        ),
    ]
