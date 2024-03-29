# Generated by Django 3.0.8 on 2020-07-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peotry',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstWord', models.CharField(default=None, max_length=64, null=True, verbose_name='输入')),
                ('result', models.CharField(max_length=256, null=True, verbose_name='输出')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '电影照片',
                'verbose_name_plural': '电影照片',
            },
        ),
    ]
