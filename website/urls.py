from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("customer/<int:pk>", views.get_customer, name="customer"),
    path("delete/<int:pk>", views.delete_customer, name="delete"),
    path("new_customer", views.new_customer, name="new_customer"),
]
