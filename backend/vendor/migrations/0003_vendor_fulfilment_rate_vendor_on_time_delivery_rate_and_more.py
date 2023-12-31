# Generated by Django 4.1.5 on 2023-12-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_purchaseorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='fulfilment_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='quality_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='response_time',
            field=models.FloatField(default=0.0),
        ),
    ]
