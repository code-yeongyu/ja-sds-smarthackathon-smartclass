# Generated by Django 2.2.4 on 2019-08-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_handle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='arduino_id',
            field=models.IntegerField(default=-1),
        ),
    ]
