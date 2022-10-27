from django.conf.urls import url
from booking import views

urlpatterns = [
    url('bkng/', views.post),
    url('ving/', views.view)

]