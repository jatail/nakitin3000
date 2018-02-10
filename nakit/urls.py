from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='FrontPage'),
    url(r'event/(?:(?P<event_id>\d+)/)?$', views.eventpage, name='EventPage'),
]