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


class Cargos(models.Model):
    nome = models.CharField(max_length=100, null=True)
    diretor_a = models.BooleanField(default=False, null=True)
    diretor_a_ass = models.BooleanField(default=False, null=True)
    secretario_a = models.BooleanField(default=False, null=True)
    tesoureiro_a = models.BooleanField(default=False, null=True)
    primeiro_anciao = models.BooleanField(default=False, null=True)
    id_membro = models.ForeignKey(Membros, on_delete=models.NOT_PROVIDED, null=True)
    anciao_jovem = models.BooleanField(default=False, null=True)
    diacono = models.BooleanField(default=False, null=True)
    diacono_chefe = models.BooleanField(default=False, null=True)
    diaconisa = models.BooleanField(default=False, null=True)
    diaconisa_chefe = models.BooleanField(default=False, null=True)
    secretario_a_ass = models.BooleanField(default=False, null=True)
    coordenador_a = models.BooleanField(default=False, null=True)
    diretor_sonoplastia = models.BooleanField(default=False, null=True)
    diretor_assistente = models.BooleanField(default=False, null=True)
    professor_a = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.nome
