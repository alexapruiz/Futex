from ast import AnnAssign
from enum import unique
from tkinter.tix import INCREASING
from tkinter.ttk import Separator
from django.db import models
from django.contrib.auth.models import User as Usuario


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True,null=False,blank=False,unique=True)
    nome = models.CharField(max_length=100,null=False,blank=False,unique=True)
    email = models.CharField(max_length=50,null=True,blank=True,unique=True)
    endereco = models.CharField(max_length=50,null=True,blank=True)
    saldo = models.DecimalField(max_digits=7,decimal_places=2, default=0)


class Historico_Cliente(models.Model):
    id_cliente      = models.IntegerField()
    id_time         = models.IntegerField()
    valor           = models.DecimalField(max_digits=6,decimal_places=2, default=0)
    tipo_operacao   = models.IntegerField()
    qtde_acoes      = models.DecimalField(max_digits=7,decimal_places=2, default=0)


class Time(models.Model):
    id_time = models.IntegerField(primary_key=True,null=False,blank=False,unique=True)
    nome    = models.CharField(max_length=30,null=False,blank=False)
    estado  = models.CharField(max_length=2,null=False,blank=False)
    valor   = models.DecimalField(max_digits=6,decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class Carteira(models.Model):
    id_cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='id_usuario',default=0)
    id_time    = models.ForeignKey(Time,on_delete=models.CASCADE,related_name='id_carteira_time')
    qtde_acoes = models.IntegerField()


class Partida(models.Model):
    id_partida = models.AutoField(primary_key=True)
    id_rodada = models.IntegerField(null=False,blank=False)
    id_time_casa  = models.ForeignKey(Time,on_delete=models.CASCADE,related_name='id_time_casa')
    id_time_visitante = models.ForeignKey(Time,on_delete=models.CASCADE,related_name='id_time_visitante')
    placar_time_casa = models.IntegerField(null=True,blank=True)
    placar_time_visitante = models.IntegerField(null=True,blank=True)


class Parametros(models.Model):
    ID_PARAMETRO = models.IntegerField(primary_key=True , default=0)
    VITORIA_CASA = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    VITORIA_FORA = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    EMPATE_CASA  = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    EMPATE_FORA  = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    DERROTA_CASA = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    DERROTA_FORA = models.DecimalField(max_digits=4,decimal_places=2, default=0)



objetos=models.Manager()