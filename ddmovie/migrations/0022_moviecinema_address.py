# Generated by Django 3.0.8 on 2020-07-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0021_auto_20200729_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecinema',
            name='address',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='地址'),
        ),
    ]