from django.db import models


class Cities(models.TextChoices):
    Tehran = 'Tehran'
    Esfehan = 'Esfahan'
    Qom = 'Qom'
    Mashhad = 'Mashhad'
    Shiraz = 'Shiraz'
    Tabriz = 'Tabriz'
    Kerman = 'Kerman'
    Ahvaz = 'Ahvaz'
