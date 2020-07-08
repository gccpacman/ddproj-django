# Generated by Django 2.2.3 on 2020-07-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0013_auto_20200708_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecinema',
            name='nameEn',
            field=models.CharField(blank=True, max_length=64, verbose_name='英文名'),
        ),
        migrations.AlterField(
            model_name='moviecinema',
            name='uri',
            field=models.CharField(max_length=128, unique=True, verbose_name='URI'),
        ),
    ]
