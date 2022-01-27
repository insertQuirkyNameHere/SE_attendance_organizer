from django.shortcuts import render
from django.views import View
from models.models import Students, ClubMemberships
# Create your views here.

class Dashboard(View):
    def get(self, request):
        curr_user = request.user
        curr_stu_obj = Students.objects.get(user=curr_user)
        club_membership_records = ClubMemberships.objects.filter(member = curr_stu_obj)
        print(curr_user)
        context = {}
        context['user'] = curr_user
        context['clubs'] = club_membership_records
        return render(request, 'student/dashboard.html', context)

class Requests(View):
    def get(self, request):
        curr_user = request.user
        curr_stu_obj = Students.objects.get(user=curr_user)
