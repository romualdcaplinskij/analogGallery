# Generated by Django 4.0.6 on 2022-08-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]