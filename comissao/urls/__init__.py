from django.urls import path, include

urlpatterns = [
    path('', include('comissao.urls.users')),
    path('', include('comissao.urls.index')),
]