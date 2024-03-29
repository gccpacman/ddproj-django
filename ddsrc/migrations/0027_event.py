# Generated by Django 2.2.3 on 2020-06-30 09:31

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0026_auto_20200518_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=128, verbose_name='事件名称')),
                ('event_uri', models.URLField(null=True, unique=True)),
                ('event_image', models.ImageField(null=True, upload_to='pic/architecture_first/', verbose_name='事件图片')),
                ('event_begin', models.DateTimeField(verbose_name='事件开始事件')),
                ('event_end', models.DateTimeField(verbose_name='事件结束事件')),
                ('raw', django_mysql.models.JSONField(default=dict, null=True, verbose_name='元数据')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '事件',
                'verbose_name_plural': '事件',
            },
        ),
    ]
