# Generated by Django 4.2.1 on 2023-08-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_logginout_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshotsmodel',
            name='image',
            field=models.FileField(upload_to='screenshots/'),
        ),
    ]