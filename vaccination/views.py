from django.shortcuts import render
from vaccination.models import Vaccination

# Create your views here.
def vaccn(request):
    if request.method == "POST":
        obj = Vaccination()
        obj.list_id='1'
        obj.date = request.POST.get('date')
        obj.time =request.POST.get('time')
        obj.age_category= request.POST.get('age')
        obj.save()
    return render(request,'vaccination/datetime.html')


def view_vaccn(request):
    obj = Vaccination.objects.all()
    context ={
        'hi' : obj
    }
    return render(request,'vaccination/view_date&timevaccine.html',context)



def stat(request,idd):
    obj = Vaccination.objects.get( vaccination_id=idd)
    obj.status='booked'
    obj.save()
    return view_vaccn(request)
