from django.urls import re_path, path, include

from . import views


urlpatterns = [
    re_path(r'editnakki/(?:(?P<nakki_id>\d+)/)?$', views.editnakki, name='Edit nakki'),
    re_path(r'editevent/(?:(?P<event_id>\d+)/)?$', views.editevent, name='Edit event'),
    re_path(r'^$', views.frontpage, name='FrontPage'),
    re_path(r'addevent/', views.addevent, name='Add event'),
    re_path(r'addnakki/(?:(?P<event_id>\d+)/)?$', views.addnakki, name='Add nakki'),
    re_path(r'event/(?:(?P<event_id>\d+)/)?$', views.eventpage, name='EventPage'),
    re_path(r'evente/(?:(?P<event_id>\d+)/)?$', views.exportnakkilaiset, name='EventPage'),
    re_path(r'regnakki/(?:(?P<nakki_id>\d+)/)?$', views.registertonakki, name='Register to Nakki'),
    re_path(r'cancelnakki/(?:(?P<nakki_id>\d+)/)?$', views.cancelnakittautuminen, name='Cancel from Nakki'),
    re_path(r'orgs/', views.orgs, name='Organization list'),
    re_path(r'signup/', views.signup, name='Sign up'),
    re_path(r'org/(?:(?P<org_id>\d+)/)?$', views.org, name='List of all events by single organizer'),
    re_path(r'profile/', views.profile, name='User profile'),
    re_path(r'^password/$', views.change_password, name='change_password'),
    path('logout/', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', include('django.contrib.auth.urls')),
]