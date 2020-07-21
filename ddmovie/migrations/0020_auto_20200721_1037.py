# Generated by Django 2.2.3 on 2020-07-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0019_auto_20200721_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviepeople',
            name='director_count',
            field=models.IntegerField(default=0, verbose_name='导演作品个数'),
        ),
        migrations.AddField(
            model_name='moviepeople',
            name='screenwriter_count',
            field=models.IntegerField(default=0, verbose_name='编剧作品个数'),
        ),
        migrations.AlterField(
            model_name='moviepeople',
            name='movie_count',
            field=models.IntegerField(default=0, verbose_name='演出作品个数'),
        ),
    ]