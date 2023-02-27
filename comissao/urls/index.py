from django.urls import path

from comissao.views import index

urlpatterns = [
    path('', index.index, name='index'),
]
