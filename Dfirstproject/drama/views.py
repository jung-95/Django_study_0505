from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from drama.models import Romance, Mystery, Disaster

def List2(request):
    R_posts2=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts2=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts2=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'R_posts2':R_posts2, 'M_posts2':M_posts2, 'D_posts2':D_posts2}
    return render(request, 'list2.html', contexts)


'''Romance의 CRUD'''

def R_edit2(request, pk):
    R_edit2 = get_object_or_404(Romance,pk=pk)
    return render(request, 'R_update2.html',{'R_edit2':R_edit2})

def R_update2(request, pk):
    R_update2= get_object_or_404(Romance,pk=pk)
    R_update2.title=request.POST['title']
    R_update2.content=request.POST['content']
    R_update2.save()
    return redirect('list2')

def R_detail2(request, pk):
    R_post2=get_object_or_404(Romance,pk=pk)
    return render(request,'R_detail2.html',{'R_post2':R_post2})

def R_new2(request):
    R_post2=Romance()
    return render(request, 'R_new2.html',{'R_post2':R_post2})

def R_create2(request):
    R_post2 =Romance()
    R_post2.title=request.POST['title']
    R_post2.author=request.POST['author']
    R_post2.upload_time=timezone.now()
    R_post2.content=request.POST['content']
    R_post2.save()
    return redirect('list2')

def R_delete2(request, pk):
    R_delete2=get_object_or_404(Romance,pk=pk)
    R_delete2.delete()
    return redirect('list2')


'''Mystery의 CRUD'''

def M_edit2(request, pk):
    M_edit2 = get_object_or_404(Mystery,pk=pk)
    return render(request, 'M_update2.html',{'M_edit2':M_edit2})

def M_update2(request, pk):
    M_update2 = get_object_or_404(Mystery,pk=pk)
    M_update2.title=request.POST['title']
    M_update2.content=request.POST['content']
    M_update2.save()
    return redirect('list2')

def M_detail2(request, pk):
    M_post2=get_object_or_404(Mystery,pk=pk)
    return render(request,'M_detail2.html',{'M_post2':M_post2})

def M_new2(request):
    M_post2=Mystery()
    return render(request, 'M_new2.html',{'M_post2':M_post2})

def M_create2(request):
    M_post2 =Mystery()
    M_post2.title=request.POST['title']
    M_post2.author=request.POST['author']
    M_post2.upload_time=timezone.now()
    M_post2.content=request.POST['content']
    M_post2.save()
    return redirect('list2')

def M_delete2(request, pk):
    M_delete2=get_object_or_404(Mystery,pk=pk)
    M_delete2.delete()
    return redirect('list2')

'''Disaster의 CRUD'''

def D_edit2(request, pk):
    D_edit2 = get_object_or_404(Disaster,pk=pk)
    return render(request, 'D_update2.html',{'D_edit2':D_edit2})

def D_update2(request, pk):
    D_update2 = get_object_or_404(Disaster,pk=pk)
    D_update2.title=request.POST['title']
    D_update2.content=request.POST['content']
    D_update2.save()
    return redirect('list2')

def D_detail2(request, pk):
    D_post2=get_object_or_404(Disaster,pk=pk)
    return render(request,'D_detail2.html',{'D_post2':D_post2})

def D_new2(request):
    D_post2=Disaster()
    return render(request, 'D_new2.html',{'D_post2':D_post2})

def D_create2(request):
    D_post2 =Disaster()
    D_post2.title=request.POST['title']
    D_post2.author=request.POST['author']
    D_post2.upload_time=timezone.now()
    D_post2.content=request.POST['content']
    D_post2.save()
    return redirect('list2')

def D_delete2(request, pk):
    D_delete2=get_object_or_404(Disaster,pk=pk)
    D_delete2.delete()
    return redirect('list2')