from django.urls import path
from . import views

app_name = 'plano_contas'

urlpatterns = [
    path('', views.PlanoContasListView.as_view(), name='list'),
    path('novo/', views.PlanoContasCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PlanoContasDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.PlanoContasUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.PlanoContasDeleteView.as_view(), name='delete'),
]
