# Generated by Django 2.2.3 on 2020-07-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0011_auto_20200707_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='formated_pub_date',
            field=models.CharField(default='', max_length=8, verbose_name='格式化的发布时间'),
        ),
    ]