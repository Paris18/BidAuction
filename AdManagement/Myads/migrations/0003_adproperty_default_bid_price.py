# Generated by Django 2.2 on 2019-04-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myads', '0002_auto_20190413_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='adproperty',
            name='default_bid_price',
            field=models.FloatField(default=True),
        ),
    ]
