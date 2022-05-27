"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import List, M_detail, D_detail, R_detail
from drama.views import List2, M_detail2, D_detail2, R_detail2
import book.views
import drama.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book',List,name='list'),
    path('book/r/<int:pk>',R_detail,name='R_detail'),
    path('book/m/<int:pk>',M_detail,name='M_detail'),
    path('book/d/<int:pk>',D_detail,name='D_detail'),
    path('drama',List2,name='list2'),
    path('drama/r/<int:pk>',R_detail2,name='R_detail2'),
    path('drama/m/<int:pk>',M_detail2,name='M_detail2'),
    path('drama/d/<int:pk>',D_detail2,name='D_detail2'),

    path('R_new/',book.views.R_new,name='R_new'),
    path('R_create/',book.views.R_create,name='R_create'),
    path('R_delete/<int:pk>',book.views.R_delete,name='R_delete'),
    path('R_edit/<int:pk>',book.views.R_edit,name='R_edit'),
    path('R_update/<int:pk>',book.views.R_update,name='R_update'),

    path('M_new/',book.views.M_new,name='M_new'),
    path('M_create/',book.views.M_create,name='M_create'),
    path('M_delete/<int:pk>',book.views.M_delete,name='M_delete'),
    path('M_edit/<int:pk>',book.views.M_edit,name='M_edit'),
    path('M_update/<int:pk>',book.views.M_update,name='M_update'),

    path('D_new/',book.views.D_new,name='D_new'),
    path('D_create/',book.views.D_create,name='D_create'),
    path('D_delete/<int:pk>',book.views.D_delete,name='D_delete'),
    path('D_edit/<int:pk>',book.views.D_edit,name='D_edit'),
    path('D_update/<int:pk>',book.views.D_update,name='D_update'),


    path('R_new2/',drama.views.R_new2,name='R_new2'),
    path('R_create2/',drama.views.R_create2,name='R_create2'),
    path('R_delete2/<int:pk>',drama.views.R_delete2,name='R_delete2'),
    path('R_edit2/<int:pk>',drama.views.R_edit2,name='R_edit2'),
    path('R_update2/<int:pk>',drama.views.R_update2,name='R_update2'),

    path('M_new2/',drama.views.M_new2,name='M_new2'),
    path('M_create2/',drama.views.M_create2,name='M_create2'),
    path('M_delete2/<int:pk>',drama.views.M_delete2,name='M_delete2'),
    path('M_edit2/<int:pk>',drama.views.M_edit2,name='M_edit2'),
    path('M_update2/<int:pk>',drama.views.M_update2,name='M_update2'),

    path('D_new2/',drama.views.D_new2,name='D_new2'),
    path('D_create2/',drama.views.D_create2,name='D_create2'),
    path('D_delete2/<int:pk>',drama.views.D_delete2,name='D_delete2'),
    path('D_edit2/<int:pk>',drama.views.D_edit2,name='D_edit2'),
    path('D_update2/<int:pk>',drama.views.D_update2,name='D_update2'),


]
