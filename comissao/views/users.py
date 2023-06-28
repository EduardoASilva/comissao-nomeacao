from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login(request):
    return render(request, 'users/login.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        if not email or not password:
            messages.error(request, 'Campos vazios')
            return redirect('login')
        usuario = User.objects.filter(email__iexact=email).last()
        if usuario:
            if usuario.is_active:
                user = auth.authenticate(username=usuario.username, password=password)
                if user is not None:
                    auth.login(request, user)
                    # save_log(request, 'Login', user, 4)
                    messages.success(request, f'Bem Vindo {user.username}')
                    return redirect('index')
                else:
                    messages.warning(request, 'Email ou Senha Incorretos.')
                    return render(request, 'users/login.html', {})
            else:
                messages.warning(request, 'Usuário inativo.')
                return render(request, 'users/login.html', {})
        else:
            messages.warning(request, 'Email incorreto ou inexistente na base de dados.')
            return redirect('login')
    else:
        return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('index')


