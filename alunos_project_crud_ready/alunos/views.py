from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm
class ListaAlunosView(generic.ListView):
    model = Aluno
    template_name = 'lista.html'
    context_object_name = 'alunos'
    ordering = ['nome']
class AlunoCreateView(generic.CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'
    success_url = reverse_lazy('lista_alunos')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Aluno criado com sucesso.')
        return response
class AlunoDetailView(generic.DetailView):
    model = Aluno
    template_name = 'aluno_detalhe.html'
    context_object_name = 'aluno'
class AlunoUpdateView(generic.UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'
    success_url = reverse_lazy('lista_alunos')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Aluno atualizado com sucesso.')
        return response
class AlunoDeleteView(generic.DeleteView):
    model = Aluno
    template_name = 'aluno_confirm_delete.html'
    success_url = reverse_lazy('lista_alunos')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Aluno excluído com sucesso.')
        return super().delete(request, *args, **kwargs)
