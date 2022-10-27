from django.conf.urls import  url
from parent import  views



urlpatterns = [
    url('pst/', views.parent),
    url('view/', views.view_prnt)

]