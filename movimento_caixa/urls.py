from django.urls import path
from . import views

app_name = 'movimento_caixa'

urlpatterns = [
    path('', views.MovimentoCaixaListView.as_view(), name='list'),
    path('novo/', views.MovimentoCaixaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MovimentoCaixaDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.MovimentoCaixaUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.MovimentoCaixaDeleteView.as_view(), name='delete'),
]
