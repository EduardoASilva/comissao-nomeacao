from django.contrib import admin
# Register your models here.
from django.contrib import admin
from comissao.models import ListaCargos, Membros


class AdminListaCargos(admin.ModelAdmin):
    list_display = ('nome',)
    list_per_page = 15

    class AdminMembros(admin.ModelAdmin):
        list_display = ('nome',)
        list_per_page = 15


admin.site.register(ListaCargos)
admin.site.register(Membros)
