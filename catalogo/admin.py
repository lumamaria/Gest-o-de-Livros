from django.contrib import admin
from .models import Livro, Autor, Genero

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Genero)