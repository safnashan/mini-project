from django.shortcuts import render
from child.models import Child
from parent.models import Parent


# Create your views here.
def post(request):
    obj =Parent.objects.all()
    context= {
        'i' : obj,
    }
    if request.method == 'POST':
        obj = Child()
        # obj.c_id='1'
        obj.p_id=request.POST.get('p')
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.dob=request.POST.get('date')
        obj.vaccination_report=request.POST.get('report')
        # obj.status='1'
        obj.save()
    return render(request,'child/detailschild.html',context)

def view(request):
    obj = Child.objects.all()
    context = {
        'bb' : obj
    }
    return render(request,'child/view_detailsofchild.html',context)


