from django.urls import path
from . import views

app_name = 'forma_pagamento'

urlpatterns = [
    path('', views.FormaPagamentoListView.as_view(), name='list'),
    path('novo/', views.FormaPagamentoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.FormaPagamentoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.FormaPagamentoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.FormaPagamentoDeleteView.as_view(), name='delete'),
]
