from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blogBody/home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogBody/detail.html',{'blog':blog})
