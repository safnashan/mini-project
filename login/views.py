from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        obj = Login()
        obj.login_id = '1'
        obj.username = request.POST.get('name')
        obj.password = request.POST.get('pass')
        obj.type = '1'
        obj.u_id = '1'
        obj.save()
    return render(request,'login/login.html')


