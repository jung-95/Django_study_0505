from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
  blogs = Blog.objects
  return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
  blog_detail = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
  return render(request, 'new.html')

def create(request):
  new_blog=Blog()
  new_blog.title = request.POST['title']
  new_blog.body = request.POST['body']
  new_blog.date = timezone.now()
  new_blog.save()
  return redirect('home')

def delete(request, blog_id):
  blog_delete = get_object_or_404(Blog, pk=blog_id)
  blog_delete.delete()
  return redirect('home')

def edit(request, blog_id):
  post = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'edit.html', {'blog':post})

def update(request, blog_id):
  blog_updated = get_object_or_404(Blog, pk=blog_id)
  blog_updated.title = request.POST['title']
  blog_updated.body = request.POST['body']
  blog_updated.save()
  return redirect("home")
