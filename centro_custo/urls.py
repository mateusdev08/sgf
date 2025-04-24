from django.urls import path
from . import views

app_name = 'centro_custo'

urlpatterns = [
    path('', views.CentroCustoListView.as_view(), name='list'),
    path('novo/', views.CentroCustoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CentroCustoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.CentroCustoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.CentroCustoDeleteView.as_view(), name='delete'),
]
