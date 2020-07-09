# Generated by Django 2.2.3 on 2020-07-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0014_auto_20200708_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviepeople',
            options={'verbose_name': '影人', 'verbose_name_plural': '影人'},
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='is_actor',
            field=models.BooleanField(default=False, verbose_name='是否演员'),
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='is_director',
            field=models.BooleanField(default=False, verbose_name='是否导演'),
        ),
        migrations.CreateModel(
            name='MoviePeopleRelation',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_uri', models.CharField(max_length=128, unique=True, verbose_name='URI')),
                ('people_uri', models.CharField(max_length=128, unique=True, verbose_name='URI')),
                ('is_director', models.BooleanField(default=False, verbose_name='是否导演')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '影人电影关系',
                'verbose_name_plural': '影人电影关系',
                'unique_together': {('movie_uri', 'people_uri')},
            },
        ),
    ]
