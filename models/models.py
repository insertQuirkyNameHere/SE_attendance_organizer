from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
user_model = get_user_model()
class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name or ''

class DepartmentMember(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    dept = models.ForeignKey(Departments, on_delete=models.CASCADE)


class Clubs(models.Model):
    name = models.CharField(max_length=50)
    president = models.OneToOneField(user_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name or ''

class Students(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    dept = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class ClubMemberships(models.Model):
    member = models.ForeignKey(Students, on_delete=models.CASCADE, unique=False)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, unique=False)

class PendingRequests(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)



class Requests(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    approval = models.BooleanField()

