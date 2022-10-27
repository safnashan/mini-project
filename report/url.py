from django.conf.urls import url
from report import  views



urlpatterns = [
    url('repot/', views.report),
    url('viw/', views.view_report)
]