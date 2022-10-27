from django.shortcuts import render
from  slot.models import Slot

# Create your views here.
def slot(request):
    if request.method == "POST":
        obj = Slot()
        obj.slot_id= '1'
        obj.list_id = '1'
        obj.date = request.POST.get('date')
        obj.time = request.POST.get('time')
        obj.save()

    return render(request,'slot/availableslot.html')


def view_slot(request):
    obj = Slot.objects.all()
    context = {
        'ff' : obj
    }
    return render(request,'slot/view_availableslot.html',context)