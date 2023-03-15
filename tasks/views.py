from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def listar(request):
    tasks = Task.objects.all()
    return render(request, "tarefas.html", {"tasks": tasks})

def create_task(request):
    tasks = Task(title=request.POST['title'], description=request.POST['description'])
    tasks.save()
    return redirect("/tasks/")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")