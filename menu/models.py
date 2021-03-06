from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.http import request
from django.conf import settings
from accounts.models import User

food_type = (
    ("veg", "veg"),
    ("nonveg", "nonveg"),
)


class menu_details(models.Model):
    restaurant = models.ForeignKey(User, help_text="", blank=True, null=True, on_delete=models.CASCADE, default='1')
    dish_name = models.CharField(blank=False, max_length=20)
    dish_type = models.CharField(max_length=10, choices=food_type, default='veg')
    price = models.CharField(blank=False, max_length=20)
    description = models.TextField(blank=True, max_length=5000, default='No Description')
    # image = models.ImageField(blank=True)

    class Meta:
        db_table = "menu_details"


class order_details(models.Model):
    customer_name = models.CharField(max_length=100, default='none')
    restaurant_name = models.CharField(max_length=100, default='none')
    dish_name = models.CharField(blank=False, max_length=20)
    dish_type = models.CharField(max_length=10, choices=food_type, default='veg')
    price = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True, max_length=5000)
    order_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "order_details"
