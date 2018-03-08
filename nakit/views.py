from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin, Eventmaker
from django.shortcuts import redirect
# Create your views here.


def frontpage(request):
    upcomingevents = Event.objects.order_by('date')
    print(upcomingevents)
    return render(request, "nakit/frontpage.html", {'upcomingevents': upcomingevents})

def eventpage(request, event_id):
    event = Event.objects.get(id=event_id)
    nakit = Nakki.objects.filter(event=event).order_by('starttime')
    nakittautumiset = Nakittautuminen.objects.filter()
    return render(request, "nakit/eventpage.html", {'event': event, 'nakit': nakit})

def registertonakki(request, nakki_id):
    nakki = Nakki.objects.get(id=nakki_id)
    event = nakki.event
    nakit = Nakki.objects.filter(event=event).order_by('starttime')
    user = request.user
    try:
        nakittautuminen = Nakittautuminen.objects.get(nakki = nakki, person = user)
    except Nakittautuminen.DoesNotExist:
        user = request.user
        nakittautuminen = Nakittautuminen(
            nakki = nakki,
            person = user,
        )
        nakittautuminen.save()
    redirectUrl = '/event/' + str(nakki.id)
    return redirect(redirectUrl)

def cancelnakittautuminen(request, nakki_id):
    nakki = Nakki.objects.get(id=nakki_id)
    user = request.user
    nakittautuminen = Nakittautuminen.objects.get(nakki = nakki, person = user)
    nakittautuminen.delete()
    redirectUrl = '/event/' + str(nakki.id)
    return redirect(redirectUrl)    