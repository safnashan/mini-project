from django.shortcuts import render
from vaccine_details.models import VaccineDetails

# Create your views here.
def vaccine(request):
    if request.method == "POST":
        obj = VaccineDetails()
        obj.vaccine_name= request.POST.get('name')
        obj.expire_date= request.POST.get('date')
        obj.details=request.POST.get('dt')
        # obj.availability = request.POST.get('avail')
        obj.save()
    return render(request,'vaccine_details/listofvaccine.html')


def view_det(request):
    obj = VaccineDetails.objects.all()
    context = {
        'abcd':obj
    }
    return render(request,'vaccine_details/view_listofvaccine.html',context)




def parent(request):
    obj = VaccineDetails.objects.all()
    context = {
        'oo':obj
    }
    return render(request,'vaccine_details/view_listofvaccine.html',context)


def avail(request,idd):
    obj = VaccineDetails.objects.get(list_id=idd)
    obj.availability='available'
    obj.save()
    return view_det(request)


def unav(request,idd):
    obj = VaccineDetails.objects.get(list_id=idd)
    obj.availability='unavailable'
    obj.save()
    return view_det(request)