# Generated by Django 3.2.9 on 2022-03-05 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_useraccount_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='profile_image',
        ),
    ]
