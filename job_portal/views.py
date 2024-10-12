from django.shortcuts import render

from .models import Job


def index(request, *args, **kwargs):
    active_jobs = Job.objects.filter(is_active=True)
    not_active_jobs = Job.objects.filter(is_active=False)
    context = {
        "active_jobs": active_jobs,
        "not_active_jobs": not_active_jobs,
    }
    return render(request, "job_portal/index.html", context)
