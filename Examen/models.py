from django.db import models

# Create your models here.
from HistoriaClinica.models import HistoriaClinica
class Examen(models.Model):
    historia_clinica= models.OneToOneField(HistoriaClinica, on_delete=models.CASCADE,primary_key=True)
    tipo= models.TextField()
    fecha= models.DateField()
    resultados= models.TextField()
    interpretacion= models.TextField()
    estado= models.TextField()
    ubicacionNodo= models.TextField()
    def __str__(self):
        return '{}'.format(self.tipo, self.fecha)