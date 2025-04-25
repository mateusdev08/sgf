from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import Cartao
from .forms import CartaoForm


class CartaoListView(ListView):
    model = Cartao
    template_name = 'cartao/list.html'
    context_object_name = 'cartoes'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['nome_cartao']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        nome_cartao = self.request.GET.get('nome_cartao')

        if nome_cartao and nome_cartao.strip():  # Verifica se não está vazio
            try:
                nome_cartao = int(nome_cartao)  # Converte para inteiro
                queryset = queryset.filter(id=nome_cartao)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome_cartao'] = Cartao.objects.all()
        return context
    # Final


class CartaoCreateView(CreateView):
    model = Cartao
    form_class = CartaoForm
    template_name = 'cartao/form.html'
    success_url = reverse_lazy('cartao:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(
            self.request, 'Cartão cadastrado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class CartaoUpdateView(UpdateView):
    model = Cartao
    form_class = CartaoForm
    template_name = 'cartao/form.html'
    success_url = reverse_lazy('cartao:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class CartaoDetailView(DetailView):
    model = Cartao
    template_name = 'cartao/detail.html'
    context_object_name = 'cartao'  # Primeira palavra no singular


class CartaoDeleteView(DeleteView):
    model = Cartao
    template_name = 'cartao/delete.html'
    success_url = reverse_lazy('cartao:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Cartao deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
