from django.contrib import admin
from models.models import ClubMemberships, Clubs, DepartmentMember,Departments, PendingRequests, Requests, Students
# Register your models here.
admin.site.register(DepartmentMember)
admin.site.register(Departments)
admin.site.register(Students)
admin.site.register(PendingRequests)
admin.site.register(Requests)
admin.site.register(ClubMemberships)
admin.site.register(Clubs)