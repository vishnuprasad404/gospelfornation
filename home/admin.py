from django.contrib import admin
from .models import Event, Photo, Video

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','title','venue','time_from','time_to','description', 'image', 'status']
    list_editable = ['title','venue','time_from','time_to', 'status']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','title','image']
    list_editable = ['title','image']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','title','image', 'link']
    list_editable = ['title','image', 'link']
