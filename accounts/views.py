from http.client import HTTPResponse
from webbrowser import get
from django.shortcuts import render,redirect
from django import views
from accounts import forms
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your views here.
UserModel = get_user_model()

class RegisterView(views.View):
    def get(self, request):
        form = forms.RegisterForm
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form['role'].value()
            print(role)
            messages.success(request, 'Registration successful.' )
            return redirect('register')
        else:
            email   = form['email'].value()
            password1 = form['password'].value()
            password2 = form['password2'].value()
            
            if UserModel.objects.filter(email=email).exists():
                messages.error(request,'Email address is already taken. Try again with a new one!')
                
            if password1 and password2 and password1 != password2:
                messages.error(request,'Passwords don\'t match')

        
        messages.error(request, 'Unsuccessful registration.')
        return redirect('register')

class LoginView(views.View):
    def get(self,request):
        form = forms.LoginForm
        return render(request, 'landing.html', {'form':form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email   = form.cleaned_data['email']
            pwd     = form.cleaned_data['password']
            user = authenticate(username=email, password=pwd)
            if user is not None:
                login(request, user)
                print('login done')
                messages.success(request, 'Login success')
                if user.is_president:
                    return redirect(reverse("pres_dash"))
                elif user.is_student:
                    return redirect(reverse("stu_dash"))
                elif user.is_dept:
                    return redirect(reverse("dept_dash"))
                else:
                    return redirect(reverse("dept_dash"))
            else:
                if UserModel.objects.filter(email=email).exists():
                    messages.error(request, 'Incorrect username or password')
                else:
                    messages.error(request, 'This user does not exist. Please register')   
                return(render(request, 'landing.html', {'form':form}))
        else:
            messages.error(request, 'email did not pass validation')
            return render(request, 'landing.html', {'form': form})

def logout_view(request):
    logout(request)
    return(redirect(reverse('home')))

class LandingPage(views.View):
    def get(self, request):
        form = forms.LoginForm
        return render(request, 'landing.html', {"form":form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email   = form.cleaned_data['email']
            pwd     = form.cleaned_data['password']
            user = authenticate(username=email, password=pwd)
            if user is not None:
                login(request, user)
                print('login done')
                messages.success(request, 'Login success')
                if user.is_president:
                    return redirect(reverse("pres_dash"))
                elif user.is_student:
                    return redirect(reverse("stu_dash"))
                elif user.is_dept:
                    return redirect(reverse("dept_dash"))
            else:
                if UserModel.objects.filter(email=email).exists():
                    messages.error(request, 'Incorrect username or password')
                else:
                    messages.error(request, 'This user does not exist. Please register')   
                return(render(request, 'landing.html', {'form':form}))
        else:
            messages.error(request, 'email did not pass validation')
            return render(request, 'landing.html', {'form': form})

