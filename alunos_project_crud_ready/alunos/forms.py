from django import forms
from .models import Aluno
import re
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: A1234'}),
        }
    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula','').strip()
        if not re.match(r'^[A-Z]\d{4}$', matricula):
            raise forms.ValidationError('A matrícula precisa ter 1 letra maiúscula seguida de 4 números (ex: A1234).')
        return matricula
