from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, ListView,\
    UpdateView, DetailView, DeleteView


class CreateJogador(CreateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'posicao_opcao',
              'cpf', 'lesoes', 'foto']


class ListJogador(ListView):
    model = Jogador
