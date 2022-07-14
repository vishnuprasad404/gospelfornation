from .models import Event, Photo, Video
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def our_minister(request):
    return render(request, 'our-minister.html')

def charity(request):
    return render(request, 'charity.html')

def services(request):
    return render(request, 'services.html')

def sacraments(request):
    return render(request, 'sacraments.html')

def events(request):
    data = {}
    queryset = Event.objects.filter(status='upcoming')
    data["upcoming_events"] = queryset
    queryset = Event.objects.filter(status='previous')
    data["previous_events"] = queryset
    return render(request, 'events.html', data)

def photos(request):
    data = {}
    queryset = Photo.objects.all()
    data["photos"] = queryset
    return render(request, 'photos.html', data)

def videos(request):
    data = {}
    queryset = Video.objects.all()
    data["videos"] = queryset
    return render(request, 'videos.html', data)

def video_details(request):
    data = {}
    id = request.GET.get('id', None)
    video = Video.objects.get(id=id)
    data["video"] = video
    return render(request, 'video_details.html', data)

def event_details(request):
    data = {}
    id = request.GET.get('id', None)
    event = Event.objects.get(id=id)
    data["event"] = event
    return render(request, 'event-details.html', data)

def about_church(request):
    return render(request, 'about-churches.html')

