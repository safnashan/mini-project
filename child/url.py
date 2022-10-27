from django.conf.urls import url
from child import  views


urlpatterns= [
    url('child/',views.post),
    url('vcld/',views.view)

]