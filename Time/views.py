from wsgiref.util import request_uri
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from Futex.models import Time
from django.shortcuts import render, redirect
from django.utils.formats import localize


@login_required(login_url='/accounts/login/')
def consultar(request):
    time = Time.objects.all()
    context = {'Times': time}
    return render(request, 'Time\index.html', context)

def criar(request):
    valor_convertido=str(request.POST['valor'].replace(",","."))
    time = Time(nome=request.POST['nome'], estado=request.POST['estado'],valor=valor_convertido)
    time.save()
    return redirect('/time')


def editar(request, id):
    if request.method == 'GET':
        time = Time.objects.get(id_time=id)
        context = {'time': time}
        return render(request, 'Time/edit.html', context)
    else:
        time = Time.objects.get(id_time=id)
        time.nome = request.POST['nome']
        time.estado = request.POST['estado']
        time.valor = str(request.POST['valor']).replace(",",".")
        time.save()
        return redirect('/time')


def excluir(request, id):
    time = Time.objects.get(id_time=id)
    time.delete()
    return redirect('/time/')