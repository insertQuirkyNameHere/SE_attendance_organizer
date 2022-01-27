from django.shortcuts import render
from django.views import View
from models.models import Students, ClubMemberships, PendingRequests, Requests
# Create your views here.

class Dashboard(View):
    def get(self, request):
        curr_user = request.user
        curr_stu_obj = Students.objects.get(user=curr_user)
        club_membership_records = ClubMemberships.objects.filter(member = curr_stu_obj)
        context = {}
        context['user'] = curr_user
        context['clubs'] = club_membership_records
        return render(request, 'student/dashboard.html', context)

class RequestsView(View):
    def get(self, request):
        curr_user = request.user
        curr_stu_obj = Students.objects.get(user=curr_user)
        pending_requests = PendingRequests.objects.filter(student=curr_stu_obj)
        requests = Requests.objects.filter(student=curr_stu_obj)
        context = {}
        context['user'] = curr_user
        context['pending_requests'] = pending_requests
        context['requests'] = requests
        return render(request, 'student/requests.html', context)
