from django.shortcuts import render
from django.http import HttpResponse


def index_cliente(request):
    return HttpResponse("Cadastro de Clientes")
