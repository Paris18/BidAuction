# Generated by Django 2.2 on 2019-04-14 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Myads', '0005_auto_20190413_2018'),
        ('biddings', '0003_auto_20190414_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinnerBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Myads.adProperty')),
                ('bidid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biddings.biddings')),
            ],
        ),
    ]
