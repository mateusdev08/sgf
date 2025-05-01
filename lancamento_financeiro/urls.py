from django.urls import path
from . import views

app_name = 'lancamento_financeiro'

urlpatterns = [
    path('', views.LancamentoFinanceiroListView.as_view(), name='list'),
    path('novo/', views.LancamentoFinanceiroCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LancamentoFinanceiroDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/',
         views.LancamentoFinanceiroUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/',
         views.LancamentoFinanceiroDeleteView.as_view(), name='delete'),
]
