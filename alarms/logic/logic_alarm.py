from EventoMedico.models import EventoMedico
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_evento_by_historia(historia):
    queryset = EventoMedico.objects.filter(historia=historia).order_by('-dateTime')[:10]
    return (queryset)

def create_alarm(historia, evento, limitExceeded):
    alarm = Alarm()
    alarm.historia_Clinica = historia
    alarm.evento = evento
    alarm.estado = evento.estado
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm