from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import ToDoForm

# Create your views here.
def index(request):

    todo = Todo.objects.filter(title__contains=request.GET.get("search",""))
    return render(request,"todo/index.html",{"todos":todo})

def create(request):
    if request.method == "GET":
        form = ToDoForm()
        return render(request,"todo/create.html",{"form":form})

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("todo")

def view(request,id):
    todo = Todo.objects.get(id=id)
    return render(request,"todo/detail.html",{"todos":todo})

def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("todo")

def edit(request,id):
    todos = Todo.objects.get(id=id)

    if request.method == "GET":
        form = ToDoForm(instance=todos)
        return render(request,"todo/edit.html",{"form":form,"id":id})
    
    if request.method == "POST":
        form = ToDoForm(request.POST,instance=todos)
        if form.is_valid:
            form.save()
        messages.success(request,"Tarea Actualizado")
        return render(request,"todo/edit.html",{"form":form,"id":id})
