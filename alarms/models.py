from django.db import models
from HistoriaClinica.models import HistoriaClinica
from EventoMedico.models import EventoMedico

class Alarm(models.Model):
    evento = models.ForeignKey(EventoMedico, on_delete=models.CASCADE, default=None)
    historia_Clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, default=None)
    estado = models.TextField()
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"evento": %s, "HistoriaClinica": %s, "limitExceeded": %s, "dateTime": %s}' % (self.evento.estado, self.historia_Clinica.medicamentosActuales, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'EventoMedico': self.evento.estado,
            'HistoriaClinica': self.historia_Clinica.medicamentosActuales,
            'estado': self.estado,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm