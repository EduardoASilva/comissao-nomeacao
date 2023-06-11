from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
