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


class Votacao(models.Model):
    votado = models.ForeignKey(Membros, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_cargo = models.ForeignKey(ListaCargos, on_delete=models.SET_NULL, null=True)
    finalizado = models.BooleanField(default=False, null=True)
    indicacao = models.BooleanField(default=False, null=True)


class ListaIndicados(models.Model):
    id_votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    id_membro_indicado = models.ForeignKey(Membros, on_delete=models.CASCADE, related_name='Membro_Indicado', null=True)
    id_membro_votou = models.ForeignKey(Membros, on_delete=models.CASCADE, related_name='Membro_Votou', null=True)





