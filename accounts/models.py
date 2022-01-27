from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_pres(self, email, password):
        if not email:
            raise ValueError('Email needs to be specified for creating an account')

        user_obj = self.model (
            email   = self.normalize_email(email)
            is_pres = True
            is_stu  = False
        )
            

        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_dept(self, email, password):
        if not email:
            raise ValueError('Email needs to specified for creating an account')

        user_obj = self.model(
            email = self.normalize_email(email)
            is_dept = True
            is_stu = False
        )

        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_stu(self, email, password):
        if not email:
            raise ValueError('Email needs to specified for creating an account')

        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_faculty(self, email, password):
        if not email:
            raise ValueError('Email needs to specified for creating an account')

        user_obj = self.model(
            email = self.normalize_email(email)
            is_stu = False
            is_faculty = True
        )

        user_obj.set_password(password)
        user_obj.save()
        return user_obj


class CustomUser (AbstractBaseUser):
    email       = models.EmailField(max_length=256, unique=True)
    active      = models.BooleanField(default=True)
    admin       = models.BooleanField(default=False)

    is_faculty  = models.BooleanField(default=False)
    is_pres     = models.BooleanField(default=False)
    is_dept     = models.BooleanField(default=False)
    is_stu      = models.BooleanField(default=True)

    USERNAME_FIELD  = 'email'
    objects         = CustomUserManager()

    def __str__(self):
        return self.email