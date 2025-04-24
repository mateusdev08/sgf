from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import CentroCusto
from .forms import CentroCustoForm


class CentroCustoListView(ListView):
    model = CentroCusto
    template_name = 'centro_custo/list.html'
    context_object_name = 'centros'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['centro_custo']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        centro_custo = self.request.GET.get('centro_custo')

        if centro_custo and centro_custo.strip():  # Verifica se não está vazio
            try:
                centro_custo = int(centro_custo)  # Converte para inteiro
                queryset = queryset.filter(id=centro_custo)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['centro_custo'] = CentroCusto.objects.all()
        return context
    # Final


class CentroCustoCreateView(CreateView):
    model = CentroCusto
    form_class = CentroCustoForm
    template_name = 'centro_custo/form.html'
    success_url = reverse_lazy('centro_custo:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(
            self.request, 'Centro de custo cadastrado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class CentroCustoUpdateView(UpdateView):
    model = CentroCusto
    form_class = CentroCustoForm
    template_name = 'centro_custo/form.html'
    success_url = reverse_lazy('centro_custo:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class CentroCustoDetailView(DetailView):
    model = CentroCusto
    template_name = 'centro_custo/detail.html'
    context_object_name = 'centro'  # Primeira palavra no singular


class CentroCustoDeleteView(DeleteView):
    model = CentroCusto
    template_name = 'centro_custo/delete.html'
    success_url = reverse_lazy('centro_custo:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Centro de custo deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
