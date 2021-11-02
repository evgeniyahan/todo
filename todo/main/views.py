from django.shortcuts import render,HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request,'test.html')

def test1(request):
    todo_list = ToDo.objects.all()
    return render(request,'test1.html',{'todo_list' : todo_list})


