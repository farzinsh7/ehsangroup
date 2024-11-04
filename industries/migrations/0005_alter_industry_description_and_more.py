# Generated by Django 4.2.4 on 2024-11-04 10:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0004_industry_description_en_industry_description_fa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='industry',
            name='description_en',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='industry',
            name='description_fa',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
