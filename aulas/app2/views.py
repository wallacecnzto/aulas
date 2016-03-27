from django.shortcuts import render
import datetime

def index(request):
    nome = 'Wallace Silva'
    data = datetime.datetime.now()
    lista = ['item1','item2','item3','item4']
    return render(request,'app2/index.html',{'nome':nome,'data':data,'lista':lista})
