from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import CreateUserForm, EmployerForm, CandidateForm
from .models import Candidate, Employer


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'jobApp/registration.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password  incorrect')

        context = {}
        return render(request, 'jobApp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    jobPosting = Employer.objects.all
    return render(request, 'jobApp/home.html', {'jobPosting': jobPosting})


@login_required(login_url='login')
def company(request):
    jobPosting = Employer.objects.all

    if request.method == 'POST':
        filled_form = EmployerForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Job posting was successful.')
            return redirect('home')

    else:
        empForm = EmployerForm()
        context = {'empForm': empForm, 'jobPosting': jobPosting}
        return render(request, 'jobApp/admin.html', context)


@login_required(login_url='login')
def account(request):
    myProfile = Candidate.objects.all
    context = {'myProfile': myProfile }
    return render(request, 'jobApp/account.html', context)


@login_required(login_url='login')
def updateAccount(request):
    profileForm = CandidateForm()

    if request.method == 'POST':
        filled_form = CandidateForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            myprofile = Candidate.objects.all
            messages.success(request, 'Profile has been updated.')
            context = {'myprofile': myprofile, 'profileForm': profileForm}

            return redirect('accounts', messages)
    else:
        profileForm = CandidateForm()
        myprofile = Candidate.objects.all
        context = {'myprofile': myprofile, 'profileForm': profileForm}

        return render(request, 'jobApp/accountUpdate.html', context)


def postJob(request):
    jobPosting = Employer.objects.all

    if request.method == 'POST':
        filled_form = EmployerForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Job posting was successful.')
            return redirect('home')

    else:
        empForm = EmployerForm()
        context = {'empForm': empForm, 'jobPosting': jobPosting}
        return render(request, 'jobApp/postJob.html', context)


def deleteJob(request, pk):

    context = {}
    return render(request, 'accounts/delete.html', context)