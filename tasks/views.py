from django.shortcuts import render, redirect, get_object_or_404
from .models import Localizacao, Eficiencia
import plotly.express as px

# Create your views here.
def home(request):
    localizacao = listar_localizacao(request)
    load_data(request)
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
        for j in range(len(meses_eficiencia[0])):
            print(meses_eficiencia[row][j][3])
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

def load_data(request):
    dados_localizacao = [
                [16.90874, 45.34907], 
                [17.15, 43.17083 ],
                [ 17.40555,	44.00693 ],
                [ 17.10456,	42.80334 ],
                [ 17.33147,	43.25468 ],
                [ 16.61088,	43.14725 ],
                [ 16.65065,	43.09689 ],
                [ 16.42765, 42.64142 ],
                [ 17.18478, 47.48398 ],
                [ 16.59708, 43.12792 ],
                [ 17.42204, 44.31632 ],
                [ 16.66667, 43.16667 ],
                [ 16.83333, 43.21667 ],
                [ 17.4,	44.01667 ],
                [ 16.83682,	43.16303 ],
                [ 17.07679,	43.19728 ],
                [ 18.74765,	50.94316 ],
                [ 17.56667,	43.43333 ],
                [ 18.86942,	51.3158 ],
                [ 17.0474, 43.19908 ],
                [ 17.56667,	43.45 ],
                [ 17.56087,	43.42968 ],
                [ 29.13139,	45.49111 ],
                [ 29.6251, 43.61596 ],
                [ 28.94117,	45.55272 ],
                [ 28.93333,	45.5 ],
                [ 29.78333,	43.88333 ],
                [ 28.88333,	45.86667 ],
                [ 28.86667,	45.45 ]
                ] # [ lat, lng ]
    
    dados_meses = [
        'Jan-21',	
        'Feb-21',	
        'Mar-21',	
        'Apr-21',	
        'May-21',	
        'Jun-21',	
        'Jul-21',	
        'Aug-21',	
        'Sep-21',	
        'Oct-21',	
        'Nov-21',	
        'Dec-21',	
        'Jan-22' ] # meses
    
    dados_eficiencia = [
        [72, 73, 70, 68, 62, 69, 75, 79, 75, 71, 72, 75, 75 ],
        [ 73, 68, 71, 68, 70, 73, 77, 80, 73, 71, 72, 45, 0 ],
        [ 77, 69, 66, 71, 70, 78, 0, 84, 75, 74, 75, 80, 80 ],
        [ 60, 56, 64, 65, 73, 81, 78, 83, 76, 75, 77, 82, 82 ],
        [ 74, 56, 64, 61, 64, 82, 79, 82, 74, 73, 75, 78, 78 ],
        [ 74, 56, 65, 60, 68, 81, 80, 83, 76, 75, 76, 79, 81 ],
        [ 67, 58, 52, 62, 69, 82, 79, 82, 75, 74, 75, 79, 80 ],
        [ 70, 59, 56, 55, 56, 77, 81, 83, 75, 74, 76, 80, 81 ],
        [ 70, 75, 58, 57, 56, 79, 76, 76, 68, 74, 75, 82, 76 ],
        [ 69, 0, 59, 59, 58, 72, 78, 91, 70, 71, 76, 77, 78 ],
        [ 79, 84, 75, 61, 59, 64, 74, 78, 68, 72, 73, 79, 75 ],
        [ 0, 86, 79, 68, 75, 69, 72, 75, 71, 69, 74, 76, 78 ],
        [ 82, 68, 81, 0, 79, 70, 71, 76, 78, 73, 72, 80, 75 ],
        [ 85, 85, 73, 74, 76, 63, 73, 84, 73, 81, 80, 84, 84 ],
        [ 67, 0, 0,	76,	77,	67,	0,	79,	75,	75,	84,	83,	80 ],
        [ 84, 85, 81, 70, 75, 66, 76, 80, 75, 77, 81, 83, 82 ],
        [ 0, 75, 78, 74, 69, 59, 74, 81, 75, 83, 84, 85, 81 ],
        [ 83, 80, 69, 0, 74, 65, 77, 80, 75, 78, 82, 83, 77 ],
        [ 80, 77, 74, 69, 74, 68, 77, 81, 79, 80, 82, 81, 87 ],
        [ 83, 77, 74, 63, 74, 67, 77, 80, 75, 79, 85, 87, 80 ],
        [ 81, 74, 74, 68, 73, 0, 77, 85, 73, 81, 82, 83, 84 ],
        [ 75, 78, 74, 72, 73, 62, 77, 81, 73, 69, 84, 86, 84 ],
        [ 73, 78, 73, 69, 73, 65, 73, 80, 76, 70, 84, 86, 87 ],
        [ 77, 63, 73, 68, 71, 67, 76, 81, 71, 72, 84, 88, 75 ],
        [ 77, 79, 73, 67, 74, 69, 76, 80, 71, 74, 86, 74, 75 ],
        [ 62, 78, 71, 67, 76, 68, 74, 81, 74, 73, 72, 75, 77 ],
        [ 76, 81, 71, 63, 75, 61, 80, 81, 74, 75, 72, 77, 75 ],
        [ 77, 76, 71, 62, 61, 72, 55, 80, 73, 73, 74, 76, 75 ],
        [ 78, 76, 76, 65, 66, 72, 77, 82, 75, 78, 73, 76, 79 ],
    ] # porcentagem


    # Carregar Localizacao
    row = 0
    column = 0
    for row in range(len(dados_localizacao[0])):
        for column in range(len(str(dados_localizacao[0][0]))):
            lat = dados_localizacao[row][0]
            lng = dados_localizacao[row][1]
            print(f'lat: {lat} | lng: {lng}')
            column = column + 1
        row = row + 1

    # localizacao = Localizacao(longitude=nova_longitude, latitude=nova_latitude)
    # localizacao.save()