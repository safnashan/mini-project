from django.shortcuts import render
from parent.models import Parent
# Create your views here.
def parent(request):
    if request.method == 'POST':
        obj = Parent()
        obj.p_id = '1'
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.username= request.POST.get('name')
        obj.e_mail = request.POST.get('mail')
        obj.password= request.POST.get('pass')
        obj.phone_no = request.POST.get('phone')
        obj.gender= request.POST.get('gender')
        obj.status = '1'
        obj.save()
    return render(request,'parent/register.html')


def view_prnt(request):
    obj = Parent.objects.all()
    context ={
        'ok' : obj
    }
    return render(request,'parent/view_registration.html',context)
