# Generated by Django 2.2.3 on 2020-07-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0016_auto_20200709_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='formated_pub_date',
            field=models.IntegerField(default=0, verbose_name='发布时间'),
        ),
    ]
