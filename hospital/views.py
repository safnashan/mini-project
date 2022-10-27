from django.shortcuts import render
from hospital.models import  Hospital

# Create your views here.
def hospital(request):
    if request.method == "POST":
        obj = Hospital()
        obj.name=request.POST.get('name')
        obj.e_mail=request.POST.get('mail')
        # obj.h_id = '1'
        obj.location= request.POST.get('location')
        obj.contact_no= request.POST.get('phone')
        obj.since = request.POST.get('year')
        obj.save()

    return render(request,'hospital/hospitalprofile.html')



def viewhosp(request):
    obj = Hospital.objects.all()
    context = {
        'cc' : obj
    }
    return render(request,'hospital/view_hospitsalprofile.html',context)