# Generated by Django 2.2.1 on 2019-07-14 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0003_architecture_road_lib_uri'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architecture',
            old_name='houseNumber',
            new_name='house_number',
        ),
    ]
