# Generated by Django 4.2.4 on 2023-11-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_description_en_company_description_fa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image_thumbnail',
            field=models.ImageField(help_text='Best size: 684*489 PX', upload_to='industry/thumbs'),
        ),
    ]