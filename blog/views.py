from django.shortcuts import render

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs })

def detail(request, blog_id):
    return blog_id #will change 
