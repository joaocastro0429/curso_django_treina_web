from django import forms

class ClientForm(forms.Form):
    nome = forms.CharField(label="Nome do cliente", max_length=100)
    idade = forms.IntegerField(label="Informe a sua idade")
    data_nascimento = forms.DateField(label="Data de nascimento")
    is_ativo = forms.BooleanField(label="O cliente está ativo?")
