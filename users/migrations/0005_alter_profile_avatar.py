# Generated by Django 4.0.6 on 2022-08-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='blankPhoto.jpg', upload_to='profile_images'),
        ),
    ]
