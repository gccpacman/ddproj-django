# Generated by Django 2.2.3 on 2020-06-23 05:05

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePhoto',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('uri', models.CharField(max_length=128, unique=True, verbose_name='URI')),
                ('raw', django_mysql.models.JSONField(default=dict, null=True, verbose_name='元数据')),
                ('filePath', models.ImageField(null=True, upload_to='', verbose_name='图片地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '剧照',
                'verbose_name_plural': '剧照',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors_uri',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director_uri',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='screen_writer_uri',
        ),
        migrations.AddField(
            model_name='movie',
            name='detail_raw',
            field=django_mysql.models.JSONField(default=dict, null=True, verbose_name='详细信息元数据'),
        ),
        migrations.AddField(
            model_name='movie',
            name='raw',
            field=django_mysql.models.JSONField(default=dict, null=True, verbose_name='元数据'),
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='nationality',
            field=models.CharField(default='', max_length=128, verbose_name='国籍'),
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='raw',
            field=django_mysql.models.JSONField(default=dict, null=True, verbose_name='元数据'),
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='speciality',
            field=models.CharField(default='', max_length=128, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='distributor',
            field=models.CharField(default='', max_length=64, verbose_name='发行商'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(default='', max_length=32, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='pub_date',
            field=models.CharField(default='', max_length=32, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='source',
            field=models.CharField(default='', max_length=64, verbose_name='来源'),
        ),
    ]
