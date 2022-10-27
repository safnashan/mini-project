from django.shortcuts import render
from  booking.models import Booking
from parent.models import Parent
from child.models import Child

# Create your views here.
def post(request):
    obj = Parent.objects.all()
    obj = Child.objects.all()
    context = {
        'h' : obj,
        'g' : obj
    }
    if request.method == "POST":
        obj = Booking()
        obj.b_id='1'
        obj.p_id='1'
        obj.c_id='1'
        obj.vaccination_id='1'
        obj.status='1'
        obj.time=request.POST.get('time')
        obj.contact_no=request.POST.get('no')
        obj.doctor_name=request.POST.get('dr')
        obj.save()

    return render(request,'booking/bookingdetails.html',context)

def view(request):
    obj = Booking.objects.all()
    context = {
        'aa' : obj
    }
    return render(request,'booking/view_bookingdetails.html',context)