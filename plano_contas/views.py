from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import PlanoContas
from .forms import PlanoContasForm


class PlanoContasListView(ListView):
    model = PlanoContas
    template_name = 'plano_contas/list.html'
    context_object_name = 'planos'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['cod_natureza']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        natureza = self.request.GET.get('natureza')

        if natureza and natureza.strip():  # Verifica se não está vazio
            try:
                natureza = int(natureza)  # Converte para inteiro
                queryset = queryset.filter(id=natureza)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['natureza'] = PlanoContas.objects.all()
        return context
    # Final


class PlanoContasCreateView(CreateView):
    model = PlanoContas
    form_class = PlanoContasForm
    template_name = 'plano_contas/form.html'
    success_url = reverse_lazy('plano_contas:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(self.request, 'Plano de contas cadastrado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class PlanoContasUpdateView(UpdateView):
    model = PlanoContas
    form_class = PlanoContasForm
    template_name = 'plano_contas/form.html'
    success_url = reverse_lazy('plano_contas:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class PlanoContasDetailView(DetailView):
    model = PlanoContas
    template_name = 'plano_contas/detail.html'
    context_object_name = 'plano'  # Primeira palavra no singular


class PlanoContasDeleteView(DeleteView):
    model = PlanoContas
    template_name = 'plano_contas/delete.html'
    success_url = reverse_lazy('plano_contas:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Plano de contas deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
