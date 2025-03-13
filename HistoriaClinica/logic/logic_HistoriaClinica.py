from .. models import HistoriaClinica
def get_historiasClinicas():
    return HistoriaClinica.objects.all()
def get_HistoriaClinica():
    queryset = HistoriaClinica.objects.all().order_by('-id')[:10]
    return (queryset)