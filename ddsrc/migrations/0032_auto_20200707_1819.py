# Generated by Django 2.2.3 on 2020-07-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0031_architecture_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architecture',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
    ]
