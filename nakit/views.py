from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin, Eventmaker
# Create your views here.


def frontpage(request):
    upcomingevents = Event.objects.order_by('date')
    print(upcomingevents)
    return render(request, "nakit/frontpage.html", {'upcomingevents': upcomingevents})

def eventpage(request, event_id):
    event = Event.objects.get(id=event_id)
    nakit = Nakki.objects.filter(event=event).order_by('starttime')
    print(event.name)
    return render(request, "nakit/eventpage.html", {'event': event, 'nakit': nakit})