from django.shortcuts import render

from .models import Job, Blog, Experience, Education

def home(request):
    jobs = Job.objects
    blogs = Blog.objects
    experience = Experience.objects
    education = Education.objects
    return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'blogs': blogs,
        'education': education,
        'experience': experience
    })
