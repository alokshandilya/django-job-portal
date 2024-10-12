from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse("<h1>Job Board</h1>")
