from django.urls import path
from . import views

app_name = 'operacao'

urlpatterns = [
    path('', views.OperacaoListView.as_view(), name='list'),
    path('novo/', views.OperacaoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.OperacaoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.OperacaoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.OperacaoDeleteView.as_view(), name='delete'),
]
