from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import *

def login(req):
    form = LoginForm()
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(req, user)
                messages.success(req, 'welcome, loged in')
                return redirect('jobs:jobs_all')
            else:
                messages.success(req, 'Failed to login')
                form = LoginForm()
    return render(req, 'accounts/login.html', context={'form': form})


def logout(req):
    auth_logout(req)
    messages.success(req, 'loged out!')
    return redirect('jobs:jobs_all')

def signup(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(req, user)
            messages.success(req, 'created')
            return redirect('profiles:profile_update', slug=req.user.profile.slug)
        else:
            messages.success(req, 'Failed to login')
            
    return render(req, 'accounts/signup.html', {'form':form})


def account(req, slug):
    

    return render(req, 'accounts/account.html', {})