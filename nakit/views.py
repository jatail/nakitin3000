from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin, Eventmaker
from django.shortcuts import redirect
from django.contrib.auth.models import User
import datetime
# Create your views here.

#tein oman rekisteröitymissivun, koska tottakai.
def signup(request):
    if request.method == 'POST':
        #vaaditaan ettei yksikään täytetyistä kentistä ole tyhjänä.
        if (request.POST.get('first') == "") or (request.POST.get('last') == "") or (request.POST.get('username') == "") or (request.POST.get('email') == "") or (request.POST.get('password1') == "") or (request.POST.get('password2') == ""):
            raiseerror = True
            errortext = 'Kaikkien kenttien tulee olla täytettynä.'
            return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})  
        try:
            #tsekataan ettei spostia ole jo käytetty.
            User.objects.get(email = request.POST.get('email'))
            raiseerror = True
            errortext = 'Sähköpostiosoitteella on jo rekisteröidytty järjestelmään.'
            return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})               
        except User.DoesNotExist:
            pass
        try:
            #tsekataan onko käyttäjänimi jo käytetty
            User.objects.get(username = request.POST.get('username'))
            raiseerror = True
            errortext = 'Käyttäjätunnus on jo varattu!'
            return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})             
        except User.DoesNotExist:
            #täsmäähän syötetyt salasanat
            if request.POST.get('password1') == request.POST.get('password2'):
                try:
                    #lopullinen rekisteröinti.
                    newuser = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
                    newuser.first_name = request.POST.get('first')
                    newuser.last_name = request.POST.get('last') 
                    newuser.save()
                    return redirect('/login')
                except:
                    raiseerror = True
                    errortext = 'Tapahtui tuntematon virhe. Ole hyvä ja yritä uudelleen. Jos ongelma toistuu ota yhteys ylläpitoon.'
                    return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})                   
            else:
                raiseerror = True
                errortext = 'Salasanat eivät täsmää!'
                return render(request, "nakit/signup.html", {'raiseerror': raiseerror, 'errortext': errortext})            
    else:
        #jos tulee http-getillä päätyy tänne.
        raiseerror = False
        return render(request, "nakit/signup.html", {'raiseerror': raiseerror})

def frontpage(request):
    upcomingevents = Event.objects.order_by('date')
    print(upcomingevents)
    return render(request, "nakit/frontpage.html", {'upcomingevents': upcomingevents})

def eventpage(request, event_id):
    event = Event.objects.get(id=event_id)
    nakit = Nakki.objects.filter(event=event).order_by('starttime')

    try:
        Orgadmin.objects.get(person=request.user, organization=event.organizer)
        orgadmin = True
    except Orgadmin.DoesNotExist:
        orgadmin = False
    #nakittautumiset = Nakittautuminen.objects.filter.select_related(nakki.event == event)
    nakittautumiset = Nakittautuminen.objects.filter(nakki__event = event)
    return render(request, "nakit/eventpage.html", {'event': event, 'nakit': nakit, 'nakittautumiset': nakittautumiset, 'orgadmin': orgadmin})

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

@login_required
def addevent(request):
    try:
        Eventmaker.objects.get(user = request.user)
    except Eventmaker.DoesNotExist:
        messagetitle = 'Ei käyttöoikeutta!'
        messagebody = 'Käyttöoikeus tapahtuman lisäämiseen puuttuu. Mikäli tarvitset oikeudet ota yhteyttä ylläpitoon.'
        return render(request, "nakit/messagepage.html", {'messagetitle': messagetitle, 'messagebody': messagebody})
    try:
        orgadmin = Orgadmin.objects.filter(person = request.user)
    except Orgadmin.DoesNotExist:
        messagetitle = 'Virhe!'
        messagebody = 'Sinua ei ole lisätty yhdenkään järjestön tapahtumajärjestäjäksi. Ota yhteyttä ylläpitoon.'
        return render(request, "nakit/messagepage.html", {'messagetitle': messagetitle, 'messagebody': messagebody})
    
    if request.method == 'POST':
        eventname = request.POST.get('eventname')
        organizer = request.POST.get('org')
        venue = request.POST.get('venue')
        description = request.POST.get('description')
        pvm = request.POST.get('pvm')
        newevent = Event(
            name = eventname,
            venue = venue,
            description = description,
            organizer = Organization.objects.get(name = organizer),
            createdby = request.user,
            date = pvm,
        )
        newevent.save()
        redirectUrl = '/event/' + str(newevent.id)
        return redirect(redirectUrl)  


    return render(request, "nakit/addevent.html", {'orgadmin': orgadmin})


@login_required
def addnakki(request, event_id):
    event = Event.objects.get(id=event_id)
    try:
        Orgadmin.objects.get(person=request.user, organization=event.organizer)
    except Orgadmin.DoesNotExist:
        messagetitle = 'Virhe!'
        messagebody = 'Sinulla ei ole oikeutta lisätä nakkia tähän tapahtumaan.'
        return render(request, "nakit/messagepage.html", {'messagetitle': messagetitle, 'messagebody': messagebody})
    if request.method == 'POST':
        task = request.POST.get('task')
        personcount = int(request.POST.get('personcount'))
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        newnakki = Nakki(
            task = task,
            event = event,
            personcount = personcount,
            starttime = starttime,
            endtime = endtime,
        )
        newnakki.save()
        showmessage = True
        messagetitle = "Nakki lisätty!"
        message = "Lisättiin uusi nakki onnistuneesti."
        return render(request, "nakit/addnakki.html", {'event': event, 'showmessage': showmessage, 'messagetitle': messagetitle, 'message': message})

    return render(request, "nakit/addnakki.html", {'event': event})
