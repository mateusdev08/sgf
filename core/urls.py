"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('conta/', include('conta.urls')),  # Se for nome composta separe com hífem, ex: plano-contas/
    path('movimento-caixa/', include('movimento_caixa.urls')),
    path('centro-custo/', include('centro_custo.urls')),
    path('cartao/', include('cartao.urls')),
    path('operacao/', include('operacao.urls')),
    path('status-movimento/', include('status_movimento.urls')),
    path('forma-pagamento/', include('forma_pagamento.urls')),
    path('plano-contas/', include('plano_contas.urls')),
    path('lancamento-financeiro/', include('lancamento_financeiro.urls')),
]
