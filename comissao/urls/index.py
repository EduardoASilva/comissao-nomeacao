from django.urls import path

from comissao.views import index

urlpatterns = [
    path('', index.index, name='index'),
    path('membros/', index.membros, name='membros'),
    path('votacao/', index.votacao, name='votacao'),
]
