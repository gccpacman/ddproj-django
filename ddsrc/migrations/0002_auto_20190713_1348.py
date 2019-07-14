# Generated by Django 2.2.1 on 2019-07-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='road',
            old_name='uri',
            new_name='lib_uri',
        ),
        migrations.AddField(
            model_name='architecture',
            name='lib_update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='architecture',
            name='lib_uri',
            field=models.URLField(null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='architecturepicture',
            name='lib_update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='architecturepicture',
            name='lib_uri',
            field=models.URLField(null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='road',
            name='lib_update_time',
            field=models.DateTimeField(null=True),
        ),
    ]