from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def listar(request):
    tasks = Task.objects.all()
    return render(
        request,
        "tarefas.html",
        {"tasks": tasks}
    )

def create_task(request):
    novo_titulo = request.POST["title"]
    nova_descricao = request.POST["description"]
    if novo_titulo == "" or nova_descricao == "":
        tasks = Task.objects.all()
        return render(
            request, "tarefas.html", {"tasks":tasks, "error":"Titulo e descrição é necessária"}
        )
    tasks = Task(title=novo_titulo, description=nova_descricao)
    tasks.save()
    return redirect("/tasks/")

def delete_task(request, task_id):
    task = Task.objects.get(task_id)
    task.delete()
    return redirect("/tasks/")