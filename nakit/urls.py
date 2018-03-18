from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'editnakki/(?:(?P<nakki_id>\d+)/)?$', views.editnakki, name='Edit nakki'),
    url(r'editevent/(?:(?P<event_id>\d+)/)?$', views.editevent, name='Edit event'),
    url(r'^$', views.frontpage, name='FrontPage'),
    url(r'addevent/', views.addevent, name='Add event'),
    url(r'addnakki/(?:(?P<event_id>\d+)/)?$', views.addnakki, name='Add nakki'),
    url(r'event/(?:(?P<event_id>\d+)/)?$', views.eventpage, name='EventPage'),
    url(r'regnakki/(?:(?P<nakki_id>\d+)/)?$', views.registertonakki, name='Register to Nakki'),
    url(r'cancelnakki/(?:(?P<nakki_id>\d+)/)?$', views.cancelnakittautuminen, name='Cancel from Nakki'),
    url(r'orgs/', views.orgs, name='Organization list'),
    url(r'signup/', views.signup, name='Sign up'),
    url(r'org/(?:(?P<org_id>\d+)/)?$', views.org, name='List of all events by single organizer'),
    url(r'profile/', views.profile, name='User profile'),
    url(r'^password/$', views.change_password, name='change_password'),

]