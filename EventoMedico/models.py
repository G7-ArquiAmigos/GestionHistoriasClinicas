from django.db import models

# Create your models here.
from HistoriaClinica.models import HistoriaClinica
class EventoMedico(models.Model):
    tipoEvento = models.TextField()
    fecha = models.DateField()
    descripcion = models.TextField()
    responsable = models.TextField()
    estado = models.TextField()
    historiaClinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.tipoEvento, self.descripcion)
