# Generated by Django 4.0.4 on 2022-05-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='helpfull',
            field=models.IntegerField(default=0),
        ),
    ]
