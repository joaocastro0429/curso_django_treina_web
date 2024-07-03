from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .forms import ClientForm

# Create your views here.


def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request, "lista_horario.html", {"horario": horario_atual})


def exibir_templates(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return HttpResponseRedirect(
                "/app/horario_atual"
            )  # return HttpResponse('cadastrado')
    else:
        form = ClientForm()

    return render(request, "form_cliente.html", {"form": form})
