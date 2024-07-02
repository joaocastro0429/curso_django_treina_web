from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def horario_atual(request):
    horario_atual=datetime.datetime.now()
    # return HttpResponse(horario_atual)
    return render(request,'lista_horario.html',{'horario':horario_atual})