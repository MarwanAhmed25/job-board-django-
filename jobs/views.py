
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import os
# Create your views here.

def jobs_all(req):
    jobs = Job.objects.all()

    return render(req, 'jobs/jobs.html', {'jobs':jobs})


@login_required
def job_create(req):
    form = JobForm()
    if req.method == 'POST':
        form = JobForm(req.POST, req.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.profile = req.user.profile
            user.save()
            messages.success(req, 'created!')
            return redirect('jobs:jobs_all')
        else:
            messages.error(req, 'faild')
            form = JobForm()
    return render(req, 'jobs/create.html', {'form':form})



def job_detail(req, slug):
    job =Job.objects.get(slug=slug)

    return render(req, 'jobs/detail.html', {'job':job})


@login_required
def job_update(req, slug):
    profile = req.user.profile
    job = profile.job_set.get(slug=slug)
    if job is not None:
        form = JobForm(instance=job)

        if req.method == 'POST':
            form = JobForm(req.POST,req.FILES, instance=job)
            if form.is_valid():
                form.save()
                messages.success(req, 'updated!')
        
                return redirect('jobs:jobs_all')
            else:
                messages.error(req, 'faild!')
                form=JobForm(instance=profile)
    else:
        messages.error(req, 'not exist')

    return render(req, 'jobs/update.html', {'form':form})


def job_delete(req, slug):
    job = Job.objects.get(slug=slug)
    if req.method=='POST':
        job.delete()
        messages.success(req, 'deleted!')
        return redirect('jobs:jobs_all')
    return render(req, 'jobs/delete.html', {})

