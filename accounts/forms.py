from django import forms
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()


class RegisterForm(forms.ModelForm):
    CHOICES=[('1','Student'),
         ('2','Club President'),
         ('3','Faculty'),
         ('4','Department')]

    role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,label="Role")



    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email','style': 'width:100%', 'class':'input_field'}))
    name = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder':'Full Name','style': 'width:100%', 'class':'input_field'}))
    password    = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder' : 'Password','style': 'width:100%', 'class':'input_field'}))
    password2   = forms.CharField(label="Confirm Password",max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','style': 'width:100%', 'class':'input_field'}))



    class Meta:
        model = User
        fields = ("email","password","password2","name","role")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password']
        )
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        print(self.cleaned_data['role'])
        if(self.cleaned_data['role'] == '1'):
            user.is_student = True
        elif(self.cleaned_data["role"] == '2'):
            user.is_student = False
            user.is_president = True
        elif(self.cleaned_data["role"] == '3'):
            user.is_student = False
            user.is_faculty = True
        elif(self.cleaned_data["role"] == '4'):
            user.is_student = False
            user.is_dept = True
        
        if commit:
            user.save()
        
        return user

class LoginForm(forms.Form):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width:100%', 'class':'input_field'}))
    password    = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style': 'width:100%', 'class':'input_field'}))

