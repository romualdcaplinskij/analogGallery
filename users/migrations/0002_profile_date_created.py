# Generated by Django 4.0.6 on 2022-08-13 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]