from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        
        verificar_usuario = auth.authenticate(
            username=usuario,
            password=senha
        )

        if(verificar_usuario != None):
            auth.logout()
            
            return redirect('index')
        else:
            print('Usuário ou senha incorretos')
            return render(request, 'pages/login.html')

    else:
        return render(request, 'pages/login.html')




def register(request):
    return render(request, 'pages/register.html')


