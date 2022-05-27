from django.contrib import admin
from book.models import Romance, Mystery, Disaster

# Register your models here.
@admin.register(Romance)
@admin.register(Mystery)
@admin.register(Disaster)

class RomanceAdmin(admin.ModelAdmin):
    romance_list=('id','title','author','upload_time','content');

class MysteryAdmin(admin.ModelAdmin):
    mystery_list=('id','title','author','upload_time','content');

class DisasterAdmin(admin.ModelAdmin):
    disaster_list=('id','title','author','upload_time','content');