from django.urls import path
from . import views
urlpatterns = [
    path('', views.ListaAlunosView.as_view(), name='lista_alunos'),
    path('novo/', views.AlunoCreateView.as_view(), name='aluno_novo'),
    path('<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detalhe'),
    path('<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_editar'),
    path('<int:pk>/excluir/', views.AlunoDeleteView.as_view(), name='aluno_excluir'),
]
