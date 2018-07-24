from django.shortcuts import render

from django.http import HttpResponse
import datetime

# Aula 3.1
from .models import Transacao

# Aula 3.2
from .form import TransacaoForm
from django.shortcuts import redirect


def home(request):
    # now = datetime.datetime.now()
    # html = '<html><body>It is now %s.</body></html>' % now
    # return HttpResponse(html)
    # return render(request, 'contas/home.html')

    data = {}

    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
	data = {}
	data['transacoes'] = Transacao.objects.all()
	return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
	form = TransacaoForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('url_listagem')

	return render(request, 'contas/form.html', {'form': form})