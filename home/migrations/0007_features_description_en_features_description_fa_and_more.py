# Generated by Django 4.2.4 on 2023-10-25 10:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='description_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='title_fa',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='about_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='about_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='mission_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='mission_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='quote_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='quote_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='sub_industries_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='sub_industries_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='title_fa',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='address_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='address_fa',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='description_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='title_fa',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_fa',
            field=models.CharField(max_length=200, null=True),
        ),
    ]