from django.conf.urls import  url
from vaccination import  views



urlpatterns = [
    url('postvc/',  views.vaccn),
    url('vdett/', views.view_vaccn),
    url('bk/(?P<idd>\w+)', views.stat),
]