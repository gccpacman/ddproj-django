# Generated by Django 2.2.3 on 2020-07-14 10:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddextra', '0002_richtextarticle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='richtextarticle',
            options={'verbose_name': '图文内容', 'verbose_name_plural': '图文内容'},
        ),
        migrations.AlterField(
            model_name='richtextarticle',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容'),
        ),
    ]