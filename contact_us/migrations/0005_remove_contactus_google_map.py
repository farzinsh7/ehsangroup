# Generated by Django 4.2.4 on 2023-10-15 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0004_alter_contactus_google_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='google_map',
        ),
    ]