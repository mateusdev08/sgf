from django.urls import path
from . import views

app_name = 'status_movimento'

urlpatterns = [
    path('', views.StatusMovimentoListView.as_view(), name='list'),
    path('novo/', views.StatusMovimentoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.StatusMovimentoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.StatusMovimentoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.StatusMovimentoDeleteView.as_view(), name='delete'),
]
