from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("greet/", views.greet),
    path("wish/", views.wish),
    path("discount/", views.calculate_discount),
    path("authors/", views.list_authors),
]
