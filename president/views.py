from django.shortcuts import render
from django.views import View
from models.models import ClubMemberships, Students, Clubs
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
