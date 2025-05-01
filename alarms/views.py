from django.http import JsonResponse
from django.shortcuts import render

from HistoriaClinica.logic.logic_HistoriaClinica import get_historia_by_id
from .logic.logic_alarm import get_alarms, get_evento_by_historia, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, historia_id):
    historia = get_historia_by_id(historia_id)
    eventos = get_evento_by_historia(historia_id)
    createAlarm = False
    upperMeasurement = None
    for evento in eventos:
        if evento.estado == "urgente":
            createAlarm = True
            upperMeasurement = evento
    if createAlarm:
        alarm = create_alarm(historia, upperMeasurement, "urgente")
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
    
