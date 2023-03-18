from django.db import models

# Create your models here.

class Localizacao(models.Model):
    longitude = models.BigIntegerField(db_column="longitude_col", null=True)
    latitude = models.BigIntegerField(db_column="latitude_col", null=True)

class Eficiencia(models.Model):
    mes = models.CharField(db_column="mes_col", max_length=20)
    porcentagem = models.BigIntegerField(db_column="eficiencia_col")
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name='localizacao')
