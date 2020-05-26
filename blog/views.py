from django.shortcuts import render, get_object_or_404
from .models import Blog
from jobs.views import setGlobal


def allblogs(request):
    gi = setGlobal()
    blogList = Blog.objects
    return render(request, 'allblogs.html', {'navName': gi['name'], 'blogList':blogList})

def blogDetail(request, blog_id):
    gi = setGlobal()
    blogDetail = get_object_or_404(Blog, pk=blog_id)
    nextBlog = blogDetail.pk + 1
    prevBlog = blogDetail.pk - 1

    return render(request, 'blogDetail.html', {'blogDetail':blogDetail,'nextBlog': nextBlog, 'prevBlog':prevBlog, 'navName': gi['name']})

def nextBlog(request):
    return render(request, 'blogDetail.html', {'nextBlog':3})
