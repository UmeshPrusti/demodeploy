from django.shortcuts import render,redirect
from enroll.models import Student
from . forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            stu = Student(name=name,email=email,password=password)
            messages.info(request,"Successfully added")
            stu.save()
            return redirect('/')
    else:
        form = StudentRegistration()
    stu = Student.objects.all()
    return render(request,'enroll/home.html',{'form':form,'stu':stu})

def delete(request,id):
    if request.method == 'POST':
        stu =  Student.objects.get(pk=id)
        stu.delete()
    return redirect('/')

def update(request,id):
    if request.method == 'POST':
        stu = Student.objects.get(pk=id)
        form = StudentRegistration(request.POST,instance=stu)
        if form.is_valid():
            messages.info(request,"Successfully updated")
            form.save()
    else:
        stu = Student.objects.get(pk=id)
        form = StudentRegistration(instance=stu)
    return render(request,'enroll/update.html',{'form':form})
