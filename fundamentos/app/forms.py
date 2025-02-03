from django import forms
from .models import Cliente

class ClientForm(forms.ModelForm):
     nome = forms.CharField(label="Nome do cliente", max_length=100)
     idade = forms.IntegerField(label="Informe a sua idade")
     data_nascimento = forms.DateField(label="Data de nascimento")
     is_ativo = forms.BooleanField(label="O cliente está ativo?")

     class Meta:
        model=Cliente
        fields=('nome','idade','data_nascimento','is_ativo')
