# Generated by Django 2.2 on 2020-05-30 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200530_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 16, 47, 36, 897831)),
        ),
    ]