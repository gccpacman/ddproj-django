# Generated by Django 2.2.3 on 2020-07-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0008_auto_20200705_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecinema',
            name='des',
            field=models.CharField(max_length=1024, verbose_name='描述'),
        ),
    ]