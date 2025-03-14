from .logic import logic_HistoriaClinica as Hl
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import HistoriaForm
from django.contrib import messages
import json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .logic.logic_HistoriaClinica import get_HistoriaClinica,  get_historiasClinicas, create_historia


# Create your views here.


@csrf_exempt
def historias_clinicas_view(request):
    if request.method == 'GET':
        historias = Hl.get_historiasClinicas()
        historias_dto = serializers.serialize('json', historias)
        return HttpResponse(historias_dto, content_type='application/json')
    

def HistoriasClinicas_list(request):
    HistoriasClinicas = get_HistoriaClinica()
    context = {
        'HistoriasClinicas_list': HistoriasClinicas
    }
    return render(request, 'HistoriaCLinica/historiaclinica.html', context)
    
def historias_create(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            create_historia(form)
            messages.add_message(request, messages.SUCCESS, 'Historia create successful')
            return HttpResponseRedirect(reverse('historiaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaForm()

    context = {
        'form': form,
    }

    return render(request, 'HistoriasClinicas/historiaCreate.html', context)