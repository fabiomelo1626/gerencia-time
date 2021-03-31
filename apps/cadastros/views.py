from django.shortcuts import render, redirect
from .models import *
from apps.gerencia.models import Especifico
from django.views.generic import CreateView, ListView,\
    UpdateView, DetailView, DeleteView


class CreateJogador(CreateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'posicao_opcao',
              'cpf', 'foto']


class ListJogador(ListView):
    model = Jogador
    # paginate_by = 100


class DetailJogador(DetailView):
    model = Jogador
