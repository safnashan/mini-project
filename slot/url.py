from django.conf.urls import  url
from  slot import  views



urlpatterns =[
    url('pst/', views.slot),
    url('viw/', views.view_slot)
]