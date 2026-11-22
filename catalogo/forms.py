from django import forms
from .models import Livro, Autor, Genero


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'ano_publicacao',
            'descricao',
            'autor',
            'genero'
        ]