# Generated by Django 2.2.3 on 2020-07-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0030_auto_20200705_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='architecture',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
