from django.urls import path
from .views import listar, create_task, delete_task

urlpatterns = [
    path('', listar),
    path('criar/', create_task, name='criar_tarefa'),
    path('deletar/<int:task_id>/', delete_task, name='delete_task')
]