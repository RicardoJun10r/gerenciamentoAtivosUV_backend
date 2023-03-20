from django.shortcuts import render, redirect, get_object_or_404
from .models import Localizacao, Eficiencia
import plotly.express as px

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
    i = 0
    meses_eficiencia = []
    for i in range(IDs.__len__()):
        meses_eficiencia.append(Eficiencia.objects.filter(localizacao_id=IDs[i]).values_list())
        i = i + 1
    meses = Eficiencia.objects.filter(localizacao_id=IDs[0]).values_list()
    axis_x = []
    for x in range(meses.__len__()):
        axis_x.append(meses[x][2])
    porcentagem = []
    row = 0
    for row in range(meses_eficiencia.__len__()):
        lista_nova = []
        for j in range(len(meses_eficiencia[0][0])):
            lista_nova.append(meses_eficiencia[row][j][3])
            j = j + 1
        porcentagem.append(lista_nova)
        row = row + 1
    fig = px.imshow(
        porcentagem,
        labels=dict(x="Meses do ano", y="ID das máquinas", color="eficiência"),
        x=axis_x,
        y=IDs,
        text_auto=True,
        )
    fig.update_xaxes(side='top')
    fig.update_layout(
        autosize = False
    )
    chart = fig.to_html()
    return render(request, "heat_map.html", {'chart': chart})

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
    novo_ano = request.POST['ano']
    nova_porcentagem = request.POST['porcentagem']
    localizacao_id = Localizacao.objects.get(id=loc_id)
    novo_mes = novo_mes + '-' + novo_ano
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