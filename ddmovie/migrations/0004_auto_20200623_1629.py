# Generated by Django 2.2.3 on 2020-06-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmovie', '0003_auto_20200623_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviephoto',
            name='filePath',
        ),
        migrations.AddField(
            model_name='moviephoto',
            name='image',
            field=models.ImageField(null=True, upload_to='movie/photos/', verbose_name='图片'),
        ),
        migrations.AddField(
            model_name='moviephoto',
            name='photoType',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]
