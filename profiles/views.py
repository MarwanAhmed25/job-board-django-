from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .forms import ProfileForm, UserForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import *
from datetime import date
import os
# Create your views here.


def profiles_all(req):
    profiles_all = Profile.objects.all()
    paginator = Paginator(profiles_all, 5)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req, 'profiles/profiles.html', {'page_obj': page_obj})


def profile_update(req, slug):

    message = ''
    user = req.user
    profile = user.profile
    
    form = ProfileForm(instance=profile)
    form2 = UserForm(instance=user)
    if req.method == 'POST':

        form = ProfileForm(req.POST, req.FILES, instance=profile)
        form2 = UserForm(req.POST, req.FILES, instance=user)
        if form.is_valid() and form2.is_valid():

            user = form2.save(commit=False)
            user.save()

            profile = form.save(commit=False)
            profile.user = user
            today = date.today()
            if profile.birthdate is not None:
                age = profile.birthdate.year
                profile.age = today.year - age
                if (today.year - age) < 20:
                    #messages.success(req, 'Your mesaage has been sent')
                    return redirect('profiles:profile_update', profile.slug)

            if profile.phone is not None:

                if len(profile.phone) != 11 and profile.phone[0] != 0 and profile.phone[1] != 1:
                    message = 'age should be enter correct phone number!!'
                    return redirect('profiles:profile_update', profile.slug)
            
            profile.save()

            auth_login(req, user)

            #messages.success(req, 'updated')
            return redirect('profiles:profile_detail', profile.slug)
        else:
            #messages.error(req, 'faild')
            return redirect('profiles:profile_update', profile.slug)

    return render(req, 'profiles/update.html', {'form': form, 'form2': form2, 'message': message})


def profile_detail(req, slug):
    print('..........')

    profile = Profile.objects.get(slug=slug)
    jobs = profile.job_set.all()
    return render(req, 'profiles/detail.html', {'profile': profile, 'jobs': jobs})


def profile_delete(req, slug):

    profile = Profile.objects.get(slug=slug)
    if req.method == 'POST':
        profile.delete()
        return redirect('accounts:login')
    return render(req, 'profiles/delete.html', {})
