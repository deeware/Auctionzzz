# Generated by Django 3.0.8 on 2020-08-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200809_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
