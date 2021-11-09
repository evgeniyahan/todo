from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, Habits


def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request,'test.html')

def test1(request):
    todo_list = ToDo.objects.all()
    return render(request,'test1.html',{'todo_list' : todo_list})

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request,'meeting.html',{'tomeet_list' : tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test1)
    
def add_meeting(request):
    form1 = request.POST
    text = form1["tomeet_text"]
    tomeet = ToMeet(persone=text)
    tomeet.save()
    return redirect(meeting)
 
def habits(request):
   habits_list = Habits.objects.all()
   return render(request,'habits.html',{'habits_list' : habits_list})

def add_habits(request):
    form2 = request.POST
    text = form2["habits_text"]
    todo = Habits(name=text)
    todo.save()
    return redirect(habits)
    




