from django.contrib import admin
from django.urls import path, include
from .views import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='stu_dash'),
]