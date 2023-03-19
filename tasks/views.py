from django.shortcuts import render, redirect, get_object_or_404
from .models import Localizacao, Eficiencia
from .utils.hashMap import HashTable

# Create your views here.
def home(request):
    localizacao = listar_localizacao(request)
    return render(request, "tarefas.html",{"localizacao": localizacao})

def dados(request):
    
    IDs = []
    equipamentos = Localizacao.objects.all().values_list()
    cont = 0

    # Pegando os IDS
    for cont in range(equipamentos.__len__()):
        IDs.append(equipamentos[cont][0])
        cont = cont + 1

    # Pegando a eficiência de cada equipamento
    hMap = HashTable(IDs.__len__()-1)
    i = 0
    for i in range(IDs.__len__()):
        hMap.set_val(IDs[i], Eficiencia.objects.filter(localizacao_id=IDs[i]).values_list())
        i = i + 1
    print(hMap)
    return render(request, "heat_map.html")

def mapa(request, loc_id):
    localizacao = Localizacao.objects.get(id=loc_id)
    return render(request, "mapbox.html", {"localizacao":localizacao})

def add_localizacao(request):
    nova_longitude = request.POST['longitude']
    nova_latitude = request.POST['latitude']
    if nova_longitude == "" or nova_latitude == "":
        localizacao = Localizacao.objects.all()
        return render(
            request, "tarefas.html/tasks/", {"localizacao": localizacao, "error": "Longitude e Latitude são necessárias!"}
        )
    localizacao = Localizacao(longitude=nova_longitude, latitude=nova_latitude)
    localizacao.save()
    return redirect("/tasks/")

def add_eficiencia(request, loc_id):
    novo_mes = request.POST['mes']
    nova_porcentagem = request.POST['porcentagem']
    localizacao_id = Localizacao.objects.get(id=loc_id)
    eficiencia = Eficiencia.objects.create(mes=novo_mes, porcentagem=nova_porcentagem, localizacao=localizacao_id)
    eficiencia.save()
    return redirect("/tasks/")

def get_localizacao(request, loc_id):
    localizacao = Localizacao.objects.get(id=loc_id)
    return render(request, "eficiencia.html", {"localizacao":localizacao})

def listar_localizacao(request):
    localizacao = Localizacao.objects.all()
    # return render(request, "tarefas.html", {"localizacao": localizacao})
    return localizacao

def listar_eficiencia(request, loc_id):
    eficiencia = Eficiencia.objects.filter(localizacao_id=loc_id)
    return render(request, "list_efic.html", {"eficiencia": eficiencia})

def deletar_localizacao(request, loc_id):
    localizacao = Localizacao.objects.get(id=loc_id)
    localizacao.delete()
    return redirect("/tasks/")