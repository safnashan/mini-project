from django.shortcuts import render
from  report.models import Report

# Create your views here.
def report(request):
    if request.method == "POST":
        obj = Report()
        obj.r_id= '1'
        obj.date = request.POST.get('date')
        obj.time = request.POST.get('time')
        obj.c_id= '1'
        obj.vaccination_id= '1'
        obj.save()

    return render(request,'report/reportvaccine.html')


def view_report(request):
    obj = Report.objects.all()
    context = {
        'ee' : obj
    }
    return render(request,'report/view_reportofvaccine.html',context)