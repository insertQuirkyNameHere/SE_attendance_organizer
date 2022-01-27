from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from models.models import ClubMemberships, Clubs, DepartmentMember, PendingRequests, Students, Requests
from django.contrib.auth import get_user_model
from django import forms
from django.urls import reverse
# Create your views here.

User = get_user_model()
class depDashboard(View):
    def get(self,request):
        curr_user  = request.user
        dept_object = DepartmentMember.objects.get(user = curr_user)
        context = {}
        context['department'] = dept_object.dept.name
        return(render(request,'department/dashboard.html',context))


class attendanceRequests(View):
    def get(self, request):
        curr_user  = request.user
        dept_object = DepartmentMember.objects.get(user = curr_user)
        students = Students.objects.filter(dept = dept_object.dept)
        requests = PendingRequests.objects.filter(student__in = students)

        return render(request,'department/attendance_requests.html',{'req' : requests})

class attendanceApproval(View):
    def post(self, request, id):
        statusAccept = self.request.POST.get("action") == "accept"
        statusReject = self.request.POST.get("action") == "reject"

        req = PendingRequests.objects.get(id = id)
        Requests.objects.create(student = req.student, club = req.club, date = req.date, approval = statusAccept)
        temp = PendingRequests.objects.get(id = id)
        temp.delete()

        return redirect(reverse('attendance_requests'))

class viewStudents(View):
    def get(self, request):
        curr_user  = request.user
        dept_object = DepartmentMember.objects.get(user = curr_user)
        students = Students.objects.filter(dept = dept_object.dept)
        clubs = ClubMemberships.objects.filter(member__in  = students)
        #data = students | clubs
        #print(data)
        return(render(request, 'department/viewstudents.html', {'clubs' : clubs}))
            
class viewStudentHistory(View):
    def get(self,request,sid,cid):
        student = Students.objects.get(id = sid)
        club = Clubs.objects.get(id = cid)

        history = Requests.objects.filter(student = student, club = club)
        
        return(render(request, 'department/viewstudenthistory.html', {'history' : history}))