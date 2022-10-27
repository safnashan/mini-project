from django.conf.urls import  url
from vaccine_details import  views



urlpatterns = [
    url('pst/', views.vaccine),
    url('viw/', views.view_det),
    url('avlbl/(?P<idd>\w+)',views.avail),
    url('prnt/',views.parent),
    url('unav/(?P<idd>\w+)',views.unav,name="unav"),
]