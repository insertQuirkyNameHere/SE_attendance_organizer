from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.depDashboard.as_view(),name='dept_dash'),
    path('requests/',views.attendanceRequests.as_view(),name = "attendance_requests"),
    path('requests/approval/<int:id>',views.attendanceApproval.as_view(), name = "attendance_approval"),
    path('students/', views.viewStudents.as_view(), name = "view_students"),
    path('students/<int:sid>/<int:cid>', views.viewStudentHistory.as_view(), name = "view_stu_history")
]