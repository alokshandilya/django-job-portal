from django.shortcuts import render, get_object_or_404

from .models import Job


def index(request, *args, **kwargs):
    active_jobs = Job.objects.filter(is_active=True)
    not_active_jobs = Job.objects.filter(is_active=False)
    context = {
        "active_jobs": active_jobs,
        "not_active_jobs": not_active_jobs,
    }
    return render(request, "job_portal/index.html", context)


def detail(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    context = {
        "job": job,
    }
    return render(request, "job_portal/detail.html", context)
