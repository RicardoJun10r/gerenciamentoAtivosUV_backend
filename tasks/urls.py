from django.urls import path
from .views import home, add_localizacao, add_eficiencia, listar_eficiencia, get_localizacao, deletar_localizacao

urlpatterns = [
    path('', home),
    path('add_loc/', add_localizacao, name='add_localizacao'),
    path('add_efi/<int:loc_id>/', add_eficiencia, name='add_eficiencia'),
    path('list_efi/', listar_eficiencia, name='list_eficiencia'),
    path('list_efi/<int:loc_id>/', listar_eficiencia, name='list_eficiencia'),
    path('buscar_loc/<int:loc_id>/', get_localizacao, name="buscar"),
    path('delete_localizacao/<int:loc_id>/', deletar_localizacao, name="deletar_loc")
]