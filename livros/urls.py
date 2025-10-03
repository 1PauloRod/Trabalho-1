from django.urls import path
from .views import emprestar_livro, MeusEmprestimosListView, LivroListAdminView, LivroCreateView, LivroUpdateView, LivroDeleteView, devolver_livro

urlpatterns = [
    #path("", LivroListView.as_view(), name="livro_list"),
    path("<int:pk>/emprestar/", emprestar_livro, name="emprestar_livro"),
    path("<int:pk>/devolver/", devolver_livro, name="devolver_livro"),
    path("emprestimos/", MeusEmprestimosListView.as_view(), name="meus_emprestimos"), 
    path("lista_livros_admin/", LivroListAdminView.as_view(), name="lista_livros_admin"),
    path("adiciona_livro_admin/", LivroCreateView.as_view(), name="adiciona_livro_admin"), 
    path("atualiza_livro_admin/<int:pk>", LivroUpdateView.as_view(), name="atualiza_livro_admin"),
    path("deleta_livro_admin/<int:pk>", LivroDeleteView.as_view(), name="deleta_livro_admin"),
]