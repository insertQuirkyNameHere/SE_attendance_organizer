from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from models.models import Students, ClubMemberships, PendingRequests, Requests
from .forms import StudentCreationForm
# Create your views here.

class Dashboard(View):
    def get(self, request):
        curr_user = request.user

        if not Students.objects.filter(user=curr_user).exists():
            form = StudentCreationForm()
            context = {}
            context['user'] = curr_user
            context['form'] = form
            return render(request, 'student/enterDetails.html', context)

        curr_stu_obj = Students.objects.get(user=curr_user)
        club_membership_records = ClubMemberships.objects.filter(member = curr_stu_obj)
        context = {}
        context['user'] = curr_user
        context['clubs'] = club_membership_records
        return render(request, 'student/dashboard.html', context)

    def post(self, request):
        curr_user = request.user
        form = StudentCreationForm(request.POST)
        student_instance = form.save(commit=False)
        student_instance.user = curr_user
        student_instance.save()
        messages.success(request, 'Student details entered successfully!')
        return redirect(reverse('stu_dash'))

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
