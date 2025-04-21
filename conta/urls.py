from django.urls import path
from . import views

app_name = 'conta'

urlpatterns = [
    path('', views.ContaListView.as_view(), name='list'),
    path('novo/', views.ContaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ContaDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.ContaUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.ContaDeleteView.as_view(), name='delete'),
]
