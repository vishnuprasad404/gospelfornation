from .models import Event, Photo, Video
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.

def home(request):
    data = {}
    queryset = Event.objects.filter(status='upcoming')
    data["upcoming_events"] = queryset
    queryset = Event.objects.filter(status='previous')
    data["previous_events"] = queryset
    return render(request, 'home.html', data)

def our_minister(request):
    return render(request, 'our-minister.html')

def charity(request):
    return render(request, 'charity.html')

def contact(request):
    return render(request, 'contact.html')

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


# message
def message_send(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        topic = request.POST['topic']
        space = " "
        newmessage = request.POST['message']

        subject = topic
        message = f"""
        {name}
        {phone}
        {email}
        {space}
        {newmessage}"""
        recipient = "wpcgospelfornations@gmail.com"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        return redirect(home)
# message end

