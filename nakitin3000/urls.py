"""nakitin3000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
#    re_path(r'^login/$', auth_views.LoginView, name='login'),
#    re_path(r'^logout/$', auth_views.LogoutView, {'next_page': '/'}, name='logout'),
#    re_path(r'^password_reset/$', auth_views.PasswordResetView, name='password_reset'),
#    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),
#    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
#    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView, name='password_reset_complete'),

    re_path(r'', include('nakit.urls')),
]
