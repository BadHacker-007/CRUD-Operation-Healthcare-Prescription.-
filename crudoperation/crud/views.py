from django.shortcuts import render
from .models import EmpModel
from django.contrib import messages
from crud.forms import Empforms


def showemp(request):
    showall = EmpModel.objects.all()
    return render(request, 'index.html', {"data": showall})


def Insertemp(request):
    if request.method == "POST":
        if request.POST.get('patientname') and request.POST.get('gender') and request.POST.get('age') and request.POST.get('medicinename') and request.POST.get('empname') and request.POST.get('price') and request.POST.get('prescription_date'):
            saverecord = EmpModel()
            saverecord.patientname = request.POST.get('patientname')
            saverecord.gender = request.POST.get('gender')
            saverecord.age = request.POST.get('age')
            saverecord.medicinename = request.POST.get('medicinename')
            saverecord.empname = request.POST.get('empname')
            saverecord.price = request.POST.get('price')
            saverecord.prescription_date = request.POST.get(
                'prescription_date')
            saverecord.save()
            messages.success(request, saverecord.patientname +
                             ' Prescription Is Saved Successfully..!')
            return render(request, 'Insert.html')
        else:
            return render(request, 'Insert.html')
    return render(request, 'Insert.html')


def Editemp(request, id):
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'Edit.html', {"EmpModel": editempobj})

def updateemp(request,id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated')
        return render(request,'Edit.html',{"EmpModel":Updateemp})

def Deleemp(request,id):
    delemployee=EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,"index.html",{"EmpModel":showdata})
