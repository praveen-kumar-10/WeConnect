# Generated by Django 3.2.9 on 2021-12-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]