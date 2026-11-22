from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    ano_publicacao = models.IntegerField()
    descricao = models.TextField()

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    def __str__(self):
        return self.titulo