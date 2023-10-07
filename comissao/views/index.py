from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from comissao.models import ListaCargos, Membros, Votacao, ListaIndicados
from comissao.templatetags.template_tags import abbreviate_name


@login_required(login_url='login')
def index(request):
    if request.user.is_staff:
        id_votacao = ''
        estagio = ''
        vota = Votacao.objects.filter(finalizado=False)
        if vota:
            vota = vota.last()
            id_votacao = vota.id
            vota = vota.id_cargo.nome
            estagio = 'indicacao'
        if request.GET.get('cancelar_votacao'):
            vota = Votacao.objects.filter(pk=request.GET.get('cancelar_votacao')).last()
            vota.delete()

        lista_cargos = ListaCargos.objects.all()
        membro = Membros.objects.all()
        context = {
            'cargos': lista_cargos,
            'membros': membro,
            'vota': vota,
            'id_votacao': id_votacao,
            'estagio': estagio

        }
        return render(request, 'index.html', context)
    else:
        vota_andamento = Votacao.objects.filter(finalizado=False)
        if vota_andamento:
            vota_andamento = vota_andamento.last()
            if ListaIndicados.objects.filter(id_votacao=vota_andamento.id, id_membro_votou_id=request.user.id):
                return render(request, 'index.html', {'votacao_em_andamento': True})
            membro = Membros.objects.filter(ativo=True, apto=True)
            context = {
                'votacao': vota_andamento,
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


def votacao(request):
    if request.GET.get('id_cargo'):
        id_cargo = request.GET.get('id_cargo')

        if not id_cargo:
            return JsonResponse({'success': False, 'msg': 'Selecione um cargo válido'})

        vota_andamento = Votacao.objects.filter(finalizado=False)
        if vota_andamento:
            vota_andamento = vota_andamento.last()

            if vota_andamento.id_cargo_id == int(id_cargo):
                return JsonResponse({
                    'success': True,
                    'id_votacao': vota_andamento.id,
                    'msg': f'Continuar com a votação {vota_andamento.id_cargo.nome} em andamento',
                    'estagio': 'indicacao'
                })
            if vota_andamento:
                return JsonResponse({
                    'success': False,
                    'msg': f'Já existe uma votação em andamento, por favor selecione {vota_andamento.id_cargo.nome} '})

        vota = Votacao.objects.create()
        vota.id_cargo_id = id_cargo
        vota.save()
        return JsonResponse({'success': True, 'msg': f'Votação do cargo {vota.id_cargo.nome} iniciada'})

    elif request.GET.get('id_membro'):
        id_membro = request.GET.get('id_membro')
        id_votacao = request.GET.get('id_votacao')
        vota = Votacao.objects.filter(pk=id_votacao).last()
        list_indicados = ListaIndicados.objects.filter(id_votacao=vota.id)
        if list_indicados:
            list_indicados = list_indicados.get()
            list_indicados.id_membro_indicado = id_membro
            list_indicados.id_membro_votou = request.user.id
            list_indicados.save()
        else:
            ListaIndicados.objects.create(
                id_votacao_id=vota.id,
                id_membro_indicado_id=id_membro,
                id_membro_votou_id=request.user.id
            )
            return JsonResponse({
                'success': True,
                'msg': f'Aguardando Votação'})
    elif request.GET.get('cancelar_votacao'):
        try:
            id_votacao = request.GET.get('cancelar_votacao')
            vota = Votacao.objects.filter(pk=id_votacao).last()
            nome = vota.id_cargo.nome
            vota.delete()
            return JsonResponse({
                'success': True,
                'msg': f'Votação para {nome} cancelado com sucesso'})
        except Exception as e:
            return JsonResponse({
                'success': False,
                'msg': f'Erro ao cancelar votação "{e.args}"'})


def verifica_estagio(request):
    if request.GET.get('estagio') == 'indicacao':
        vota = Votacao.objects.filter(pk=request.GET.get('id_votacao')).last()
        indicados = ListaIndicados.objects.filter(id_votacao_id=vota.id)
        data = []
        for i in indicados:
            nome = abbreviate_name(i.id_membro_indicado.nome)
            itens = {'id_membro': i.id_membro_indicado_id, 'nome_membro': nome}
            data.append(itens)
        context = {
            'data': data
        }
        return JsonResponse(context)
