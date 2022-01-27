from django.contrib import admin
from django.urls import path, include
from .views import Dashboard, RequestsView

urlpatterns = [
    path('', Dashboard.as_view(), name='stu_dash'),
    path('requests/', RequestsView.as_view(), name='stu_requests'),

]