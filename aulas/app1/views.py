from django.shortcuts import render
from django.http import HttpResponse
import datetime
def ola_mundo(request):
    texto = 'Olá Mundo'
    return HttpResponse(texto)

def soma(request):
    a = 10
    b = 10
    c = a + b
    return HttpResponse('a=%d+b=%d=%d'%(a,b,c))

def data_hora(request):
    now = datetime.datetime.now().strftime('%d-%m=%Y%H:%M:%S')
    html = "<html><body>Hoje é: %s.</body></html>"%now
    return HttpResponse(html)

def status_code(request):
    status = HttpResponse.status_code
    return HttpResponse('A pagina respondeu: %s'%status)
