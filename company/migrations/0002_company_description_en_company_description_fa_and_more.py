# Generated by Django 4.2.4 on 2023-10-25 09:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='keywords_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='keywords_fa',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='seo_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='seo_description_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='title_fa',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
