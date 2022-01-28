from django.contrib import admin
from django.urls import path
from.views import Dashboard, ViewMembers, AddMembers, ManageMembers, AttendanceView

urlpatterns = [
    path('', Dashboard.as_view(), name='pres_dash'),
    path('club/<int:clubId>/', ViewMembers.as_view(), name='club_view'),
    path('club/<int:clubId>/addMembers/', AddMembers.as_view(), name='add_members'),
    path('club/<int:clubId>/<int:memberId>/', ManageMembers.as_view(), name='manage_members'),
    path('club/<int:clubId>/<int:memberId>/attendance', AttendanceView.as_view(), name='members_attendance'),
]