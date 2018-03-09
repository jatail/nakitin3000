from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin, Eventmaker
from django.shortcuts import redirect
from django.contrib.auth.models import User
import datetime
# Create your views here.

def signup(request):
    if request.method == 'POST':
        print("Password 1:", request.POST.get('password1'))
        if request.POST.get('password1') == request.POST.get('password2'):
            newuser = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
            newuser.first_name = request.POST.get('first')
            newuser.last_name = request.POST.get('last') 
            newuser.save()
            return redirect('/')
        else:
            raiseerror = True
            errortext = 'Salasanat eivät täsmää!'
            return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})            
    else:
        raiseerror = False
        return render(request, "nakit/signup.html", {'raiseerror': raiseerror})

def frontpage(request):
    upcomingevents = Event.objects.order_by('date')
    print(upcomingevents)
    return render(request, "nakit/frontpage.html", {'upcomingevents': upcomingevents})

def eventpage(request, event_id):
    event = Event.objects.get(id=event_id)
    nakit = Nakki.objects.filter(event=event).order_by('starttime')
    #nakittautumiset = Nakittautuminen.objects.filter.select_related(nakki.event == event)
    nakittautumiset = Nakittautuminen.objects.filter(nakki__event = event)
    return render(request, "nakit/eventpage.html", {'event': event, 'nakit': nakit, 'nakittautumiset': nakittautumiset})

@login_required
def registertonakki(request, nakki_id):
    nakki = Nakki.objects.get(id=nakki_id)
    event = nakki.event
    nakit = Nakki.objects.filter(event=event).order_by('starttime')
    user = request.user
    if Nakittautuminen.objects.filter(nakki = nakki).count() >= nakki.personcount:
        pass
    else:
        try:
            nakittautuminen = Nakittautuminen.objects.get(nakki = nakki, person = user)
        except Nakittautuminen.DoesNotExist:
            user = request.user
            nakittautuminen = Nakittautuminen(
                nakki = nakki,
                person = user,
            )
            nakittautuminen.save()
    redirectUrl = '/event/' + str(event.id)
    return redirect(redirectUrl)

@login_required
def cancelnakittautuminen(request, nakki_id):
    nakki = Nakki.objects.get(id=nakki_id)
    user = request.user
    event = nakki.event
    nakittautuminen = Nakittautuminen.objects.get(nakki = nakki, person = user)
    nakittautuminen.delete()
    redirectUrl = '/event/' + str(event.id)
    return redirect(redirectUrl)    

def orgs(request):
    organizations = Organization.objects.filter().order_by('name')
    return render(request, "nakit/orgs.html", {'organizations': organizations})

def org(request, org_id):
    organizer = Organization.objects.get(id=org_id)
    now=datetime.datetime.now()
    events_upcoming = Event.objects.filter(organizer=organizer)
    events_past = Event.objects.filter(organizer=organizer)

    return render(request, "nakit/org.html", {'events_upcoming': events_upcoming, 'events_past' : events_past, 'org_name': organizer.name})