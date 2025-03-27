from django.shortcuts import render
from .models import Contato
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):

    contatos = Contato.objects.all()

    return render(request, 'pages/index.html', {'contatos':contatos})
