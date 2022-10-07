from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^registration/$', views.user_registration, name='registration'),
]
