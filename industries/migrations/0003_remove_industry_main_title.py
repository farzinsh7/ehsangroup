# Generated by Django 4.2.4 on 2023-10-03 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0002_industry_main_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='main_title',
        ),
    ]