from django.shortcuts import render

from .models import Job, Blog

def home(request):
    jobs = Job.objects
    blogs = Blog.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'blogs': blogs })
