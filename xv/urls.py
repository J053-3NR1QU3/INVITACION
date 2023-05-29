from django.contrib import admin
from django.urls import path
from xv.views import invitacion, invitados,confirmacion

urlpatterns = [
    path('', invitacion, name="invitacion"),
    path('invitados/',invitados, name="invitados"),
    path('confirmacion/',confirmacion,name="confirmacion"),
]