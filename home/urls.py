from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('minister', views.our_minister),
    path('charity', views.charity),
    path('events', views.events),
    path('event/details', views.event_details),
    path('services', views.services),
    path('photos', views.photos),
    path('videos', views.videos),
    path('video/details', views.video_details),
    path('event/details', views.event_details),
    path('sacraments', views.sacraments),
    path('church/about', views.about_church),
    path('contact', views.contact),

]
