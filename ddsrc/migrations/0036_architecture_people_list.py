# Generated by Django 2.2.3 on 2020-07-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0035_auto_20200709_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='architecture',
            name='people_list',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='相关人物'),
        ),
    ]
