# Generated by Django 2.2.12 on 2020-05-28 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200528_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_details',
            name='restaurant_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
