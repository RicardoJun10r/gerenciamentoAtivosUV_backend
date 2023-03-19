from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django import template
from .views import hMap_dados

register = template.Library()



def mostrar_valores():
    hmap = hMap_dados()
    return {'hmap': hmap}

heatMap_template = get_template('heat_map.html')
register.inclusion_tag(heatMap_template)(mostrar_valores)