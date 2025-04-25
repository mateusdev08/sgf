from django.urls import path
from . import views

app_name = 'cartao'

urlpatterns = [
    path('', views.CartaoListView.as_view(), name='list'),
    path('novo/', views.CartaoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CartaoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.CartaoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.CartaoDeleteView.as_view(), name='delete'),
]
