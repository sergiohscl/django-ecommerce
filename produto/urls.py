from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('add_carrinho/', views.AddCarrinho.as_view(), name="add_carrinho"),
    path(
        'remove_carrinho/',
        views.RemoveCarrinho.as_view(),
        name="remove_carrinho"
    ),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('resumo_compra/', views.ResumoCompra.as_view(), name="resumo_compra"),
    path('busca/', views.Busca.as_view(), name="busca"),
]
