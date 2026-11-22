from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),

    path('autores/', views.autores, name='autores'),

    path('generos/', views.generos, name='generos'),

    path('livros/', views.livros, name='livros'),

    path('livro/<int:id>/', views.detalhes_livro, name='detalhes_livro'),
]