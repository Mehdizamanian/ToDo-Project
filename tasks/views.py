from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Task
from .forms import Taskform

def taskview (request):
    task = Task.objects.all()
    form=Taskform()

    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'tasks/tasks.html',{'task':task ,'form':form})


def delete (request , pk ):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')




def upgrade(request , pk):
    task=Task.objects.get(id=pk)
    form=Taskform(instance=task)

    if request.method=='POST':
        form=Taskform(request.POST , instance=task)
        if form . is_valid():
            form.save()
            return redirect ('/')


    return render(request,'tasks/upgrade.html',{'form':form})


# Create your views here.
