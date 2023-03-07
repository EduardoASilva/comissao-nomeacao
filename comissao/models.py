from django.db import models


class Cargos(models.Model):
    name = models.CharField(max_length=100)

