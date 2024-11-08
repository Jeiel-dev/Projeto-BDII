from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User_log


def register_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return render(request, 'register.html', {'passNot': True})

        try:
            user = User_log(name=nome, email=email)
            user.set_password(senha)  # Define a senha de forma segura
            user.save()
            return redirect('logar')
        except Exception as e:
            return render(request, 'register.html', {'jaCad': True})

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = User_log.objects.get(email=email)
            if user.check_password(senha):  # Verifica a senha
                return HttpResponse('success')
            else:
                return render(request, 'login.html', {'userNot': True})
        except User_log.DoesNotExist:
            return render(request, 'login.html', {'userNot': True})

    return render(request, 'login.html')
