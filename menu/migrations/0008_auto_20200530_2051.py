# Generated by Django 2.2 on 2020-05-30 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20200530_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 20, 51, 27, 431466)),
        ),
    ]