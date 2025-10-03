from django.db import models
from django.conf import settings

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    def str(self):
        return f"{self.titulo} - {self.autor}"
    

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.livro} emprestado por {self.usuario.email}"
