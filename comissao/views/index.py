from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from comissao.models import ListaCargos, Membros


@login_required(login_url='login')
def index(request):
    if request.user.is_staff:
        lista_cargos = ListaCargos.objects.all()
        membro = Membros.objects.all()
        context = {
            'cargos': lista_cargos,
            'membros': membro
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


@login_required(login_url='login')
def membros(request):
    membro = Membros.objects.all()
    context = {
        'membros': membro
    }
    return render(request, 'membros.html', context)
