from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from comissao.models import ListaCargos


@login_required(login_url='login')
def index(request):
    if request.user.is_staff:
        lista_cargos = ListaCargos.objects.all()
        context = {
            'cargos': lista_cargos
        }
        return render(request, 'index.html', context)
    else:
        pass
