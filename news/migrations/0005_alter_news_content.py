# Generated by Django 5.1.1 on 2024-09-24 09:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Kontent'),
        ),
    ]
