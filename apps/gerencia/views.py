from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView, ListView,\
    UpdateView, DetailView, DeleteView
import matplotlib.pyplot
from django.contrib.auth.decorators import login_required


class CreateScore(CreateView):
    model = Scores
    fields = '__all__'


@login_required
def JogadorScores(request, id):
    object = Jogador.objects.get(pk=id)
    context = {
        'object': object
    }
    return render(request, 'gerencia/scores_detail.html', context)


@login_required
def grafico(request, id):
    form = Scores.objects.get(pk=id)
    passe =(5,8,7,12,5)
    time = ('dia1', 'dia2', 'dia3', 'dia4', 'dia5')
    nome = form.jogador.nome
    matplotlib.pyplot.title(nome)
    matplotlib.pyplot.plot(time, passe)
    matplotlib.pyplot.show()
    return redirect('gerencia:list_scores')


class CreateEspecifico(CreateView):
    model = Especifico
    fields = '__all__'


class DetailEspecifico(DetailView):
    model = Especifico
