from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from book.models import Romance, Mystery, Disaster

def List(request):
    R_posts=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'R_posts':R_posts, 'M_posts':M_posts, 'D_posts':D_posts}
    return render(request, 'list.html', contexts)

'''Romance의 CRUD'''

def R_edit(request, pk):
    R_edit = get_object_or_404(Romance,pk=pk)
    return render(request, 'R_update.html',{'R_edit':R_edit})

def R_update(request, pk):
    R_update = get_object_or_404(Romance,pk=pk)
    R_update.title=request.POST['title']
    R_update.content=request.POST['content']
    R_update.save()
    return redirect('list')

def R_detail(request, pk):
    R_post=get_object_or_404(Romance,pk=pk)
    return render(request,'R_detail.html',{'R_post':R_post})

def R_new(request):
    R_post=Romance()
    return render(request, 'R_new.html',{'R_post':R_post})

def R_create(request):
    R_post =Romance()
    R_post.title=request.POST['title']
    R_post.author=request.POST['author']
    R_post.upload_time=timezone.now()
    R_post.content=request.POST['content']
    R_post.save()
    return redirect('list')

def R_delete(request, pk):
    R_delete=get_object_or_404(Romance,pk=pk)
    R_delete.delete()
    return redirect('list')


'''Mystery의 CRUD'''

def M_edit(request, pk):
    M_edit = get_object_or_404(Mystery,pk=pk)
    return render(request, 'M_update.html',{'M_edit':M_edit})

def M_update(request, pk):
    M_update = get_object_or_404(Mystery,pk=pk)
    M_update.title=request.POST['title']
    M_update.content=request.POST['content']
    M_update.save()
    return redirect('list')

def M_detail(request, pk):
    M_post=get_object_or_404(Mystery,pk=pk)
    return render(request,'M_detail.html',{'M_post':M_post})

def M_new(request):
    M_post=Mystery()
    return render(request, 'M_new.html',{'M_post':M_post})

def M_create(request):
    M_post =Mystery()
    M_post.title=request.POST['title']
    M_post.author=request.POST['author']
    M_post.upload_time=timezone.now()
    M_post.content=request.POST['content']
    M_post.save()
    return redirect('list')

def M_delete(request, pk):
    M_delete=get_object_or_404(Mystery,pk=pk)
    M_delete.delete()
    return redirect('list')


'''Disaster의 CRUD'''

def D_edit(request, pk):
    D_edit = get_object_or_404(Disaster,pk=pk)
    return render(request, 'D_update.html',{'D_edit':D_edit})

def D_update(request, pk):
    D_update = get_object_or_404(Disaster,pk=pk)
    D_update.title=request.POST['title']
    D_update.content=request.POST['content']
    D_update.save()
    return redirect('list')

def D_detail(request, pk):
    D_post=get_object_or_404(Disaster,pk=pk)
    return render(request,'D_detail.html',{'D_post':D_post})

def D_new(request):
    D_post=Disaster()
    return render(request, 'D_new.html',{'D_post':D_post})

def D_create(request):
    D_post =Disaster()
    D_post.title=request.POST['title']
    D_post.author=request.POST['author']
    D_post.upload_time=timezone.now()
    D_post.content=request.POST['content']
    D_post.save()
    return redirect('list')

def D_delete(request, pk):
    D_delete=get_object_or_404(Disaster,pk=pk)
    D_delete.delete()
    return redirect('list')
