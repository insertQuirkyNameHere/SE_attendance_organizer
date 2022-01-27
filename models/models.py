from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user_model = get_user_model()
class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Clubs(models.Model):
    name = models.CharField(max_length=50)
    president = models.OneToOneField(user_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Students(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    dept = models.OneToOneField(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class ClubMemberships(models.Model):
    member = models.ForeignKey(Students, on_delete=models.CASCADE, unique=False)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, unique=False)

class PendingRequests(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date = models.DateField()

class Requests(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    date = models.DateField()
    approval = models.BooleanField()

