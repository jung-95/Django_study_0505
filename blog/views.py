from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, HashTag
from django.utils import timezone
from .forms import BlogForm, CommentForm

def add_comment(request, blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)

  if request.method == 'POST':
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = blog
      comment.save()
      return redirect('detail', blog_id)

  else:
    form = CommentForm()

  return render(request, 'add_comment.html', {'form':form})

# Create your views here.

def home(request):
  blogs = Blog.objects
  return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
  blog_detail = get_object_or_404(Blog, pk=blog_id)
  blog_hashtag = blog_detail.hashtag.all()
  return render(request, 'detail.html', {'blog':blog_detail, 'hashtags':blog_hashtag})

def new(request):
  return render(request, 'new.html')

def create(request):
  form = BlogForm(request.POST, request.FILES)
  if form.is_valid():
    new_blog=form.save(commit=False)
    new_blog.title = request.POST['title']
    new_blog.body = request.POST['body']
    new_blog.date = timezone.now()
    new_blog.save()
    hashtags = request.POST['hashtags']
    hashtag = hashtags.split(", ")
    for tag in hashtag:
      new_hashtag = HashTag()
      new_hashtag.hashtag=tag
      new_hashtag.save()
      new_blog.hashtag.add(new_hashtag)
    return redirect('detail', new_blog.id)
  return redirect('home')

def delete(request, blog_id):
  blog_delete = get_object_or_404(Blog, pk=blog_id)
  blog_delete.delete()
  return redirect('home')

def edit(request, blog_id):
  post = get_object_or_404(Blog, pk=blog_id)
  hash = get_object_or_404(HashTag, pk=blog_id)
  return render(request, 'edit.html', {'blog':post, 'hashtags':hash})

def update(request, blog_id):
  blog_updated = get_object_or_404(Blog, pk=blog_id)
  blog_updated.title = request.POST['title']
  blog_updated.body = request.POST['body']
  hashtags = request.POST['hashtags']
  hashtag = hashtags.split(", ")
  for tag in hashtag:
    updated_hashtag = HashTag()
    updated_hashtag.hashtag = tag
    updated_hashtag.save()
    blog_updated.hashtag.add(updated_hashtag)
  return redirect('detail', blog_updated.id)


