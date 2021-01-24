from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employer, Candidate


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        exclude = ['candidate']


class ResumeUpload(forms.Form):
    title = forms.CharField(max_length=50)
    resume = forms.FileField()


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        exclude = ['user']

