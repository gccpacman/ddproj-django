# Generated by Django 2.2.3 on 2020-07-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0036_architecture_people_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architecture',
            name='first_image_path',
            field=models.ImageField(blank=True, null=True, upload_to='pic/architecture_first/'),
        ),
    ]
