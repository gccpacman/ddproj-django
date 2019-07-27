# Generated by Django 2.2.1 on 2019-07-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0010_auto_20190715_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='architecture',
            name='first_image_lib_uri',
            field=models.URLField(null=True, verbose_name='首页照片图书馆URI'),
        ),
        migrations.AddField(
            model_name='architecture',
            name='lib_is_red',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='architecture',
            name='des2',
            field=models.TextField(blank=True, null=True, verbose_name='简介(手动编辑)'),
        ),
        migrations.AlterField(
            model_name='architecture',
            name='first_image_uri',
            field=models.URLField(null=True, verbose_name='首页照片网址'),
        ),
        migrations.AlterField(
            model_name='architecturepicture',
            name='des',
            field=models.TextField(blank=True, null=True, verbose_name='简介(上海图书馆数据)'),
        ),
        migrations.AlterField(
            model_name='architecturepicture',
            name='des2',
            field=models.TextField(blank=True, null=True, verbose_name='简介(手动编辑)'),
        ),
        migrations.AlterField(
            model_name='architecturepicture',
            name='pic_format',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]