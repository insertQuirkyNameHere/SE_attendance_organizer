from importlib.resources import contents
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from matplotlib.style import context
from models.models import ClubMemberships, PendingRequests, Students, Clubs
from django.contrib import messages
# Create your views here.

class Dashboard(View):
    def get(self, request):
        curr_user = request.user
        curr_stu_obj = Students.objects.get(user=curr_user)
        club_leadership_records = Clubs.objects.filter(president=curr_user)
        club_membership_records = ClubMemberships.objects.filter(member=curr_stu_obj)
        context = {}
        context['user'] = curr_user
        context['leadClubs'] = club_leadership_records
        context['clubs'] = club_membership_records
        return render(request, 'president/dashboard.html', context)

class ViewMembers(View):
    def get(self, request, clubId):
        curr_user = request.user
        club_obj = Clubs.objects.get(id=clubId)
        club_members_obj = ClubMemberships.objects.filter(club=club_obj)
        context = {}
        context['club'] = club_obj
        context['user'] = curr_user
        context['members'] = club_members_obj
        return render(request, 'president/memberList.html', context)

class AddMembers(View):
        def get(self, request, clubId):
            curr_user = request.user
            club_obj = Clubs.objects.get(id=clubId)
            club_members_obj = ClubMemberships.objects.filter(club=club_obj)
            all_students_obj = Students.objects.all()
            context = {}
            context['user']  = curr_user
            context['club'] = club_obj
            context['students'] = all_students_obj
            context['members'] = club_members_obj
            return render(request, 'president/addMembers.html', context)

        def post(self, request, clubId):
            received_student = request.POST.get('student')
            received_student = Students.objects.get(id=received_student)
            club_obj = Clubs.objects.get(id=clubId)
            if ClubMemberships.objects.filter(member=received_student, club=club_obj).exists():
                messages.error(request, 'This dude is already a part of your club, dinkus!')
                return redirect(reverse('add_members', args=(clubId, )))
            else:
                newEntry = ClubMemberships(member=received_student, club=club_obj)
                newEntry.save()
                messages.success(request, 'New Member added')
                return redirect(reverse('add_members', args=(clubId, )))

class ManageMembers(View):
    def get(self, request, clubId, memberId):
        curr_user = request.user
        club_obj = Clubs.objects.get(id=clubId)
        member_obj = ClubMemberships.objects.get(club=club_obj, member=memberId)
        context = {}
        context['user'] = curr_user
        context['club'] = club_obj
        context['member'] = member_obj
        return render(request, 'president/manageMembers.html', context)

    def post(self, request, clubId, memberId):
        stu_obj = Students.objects.get(id=memberId)
        club_obj = Clubs.objects.get(id=clubId)
        print(request.POST)
        if 'del' in request.POST:
            ClubMemberships.objects.get(member=stu_obj, club=club_obj).delete()
            PendingRequests.objects.filter(student=stu_obj, club=club_obj).delete()
            messages.info(request, 'Member successfully deleted')
            return redirect(reverse('club_view', args=(clubId, )))
        if 'req_att' in request.POST:
            newEntry = PendingRequests(
                student = stu_obj,
                club = club_obj,
                date = request.POST.get('date'), 
            )
            newEntry.save()
            messages.info(request, 'Attendance requested successfully!')
            return redirect(reverse('club_view', args=(clubId, )))
        return redirect(reverse('club_view', args=(clubId, )))

