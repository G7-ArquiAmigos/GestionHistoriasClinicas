from .logic import logic_HistoriaClinica as Hl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .logic.logic_HistoriaClinica import get_HistoriaClinica,  get_historiasClinicas


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
    