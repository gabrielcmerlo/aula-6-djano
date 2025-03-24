from django.shortcuts import render
from .models import Contato

def index(request):

    contatos = Contato.objects.all()

    return render(request, 'pages/index.html', {'contatos':contatos})
