# Generated by Django 2.2.1 on 2019-08-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0023_auto_20190729_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='history_of_name',
            field=models.CharField(max_length=64, null=True, verbose_name='历史关联'),
        ),
        migrations.AlterField(
            model_name='road',
            name='name_chs',
            field=models.CharField(max_length=64, unique=True, verbose_name='中文名'),
        ),
    ]
