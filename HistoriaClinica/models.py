from django.db import models

# Create your models here.
class HistoriaClinica(models.Model):
    antecedentesMedicos = models.TextField()
    medicamentosActuales = models.TextField()
    alergias = models.TextField()
    cirugiasPrevias = models.TextField()
    notasAdicionales = models.TextField()
    def __str__(self):
        return '{}'.format(self.antecedentesMedicos)
