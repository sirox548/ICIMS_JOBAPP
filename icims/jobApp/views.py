from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm


def home(request):
    return render(request, 'jobApp/home.html')


def company(request):
    return render(request, 'jobApp/admin.html')


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'jobApp/registration.html', context)


def login(request):
    return render(request, 'jobApp/login.html')


