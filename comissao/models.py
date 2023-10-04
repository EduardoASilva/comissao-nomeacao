from django.db import models


class Membros(models.Model):
    nome = models.CharField(max_length=100, null=True)
    ativo = models.BooleanField(default=True)
    apto = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class ListaCargos(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome


class MembroCargos(models.Model):
    id_membro = models.ForeignKey(Membros, on_delete=models.NOT_PROVIDED, null=True)
    id_cargo = models.ForeignKey(ListaCargos, on_delete=models.NOT_PROVIDED, null=True)


class Votacao(models.Model):
    