from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('restaurant_register/', views.restaurant_register.as_view(), name='restaurant_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
