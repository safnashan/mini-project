from django.conf.urls import url
from hospital import views



urlpatterns = [
    url('profile/', views.hospital),
    url('viewhospitl/', views.viewhosp)
]