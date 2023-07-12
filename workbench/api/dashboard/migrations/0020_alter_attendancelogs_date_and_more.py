# Generated by Django 4.2.1 on 2023-07-11 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_alter_attendancelogs_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancelogs',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
        ),
        migrations.AlterField(
            model_name='attendancelogs',
            name='login_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
        ),
        migrations.AlterField(
            model_name='attendancelogs',
            name='logout_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
        ),
        migrations.AlterField(
            model_name='attendancelogs',
            name='work_status',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
        ),
    ]