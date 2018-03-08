from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='FrontPage'),
    url(r'event/(?:(?P<event_id>\d+)/)?$', views.eventpage, name='EventPage'),
    url(r'regnakki/(?:(?P<nakki_id>\d+)/)?$', views.registertonakki, name='Register to Nakki'),
    url(r'cancelnakki/(?:(?P<nakki_id>\d+)/)?$', views.cancelnakittautuminen, name='Cancel from Nakki'),
]