# Generated by Django 2.2.1 on 2019-07-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddsrc', '0007_auto_20190715_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architecture',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='英文名'),
        ),
    ]
