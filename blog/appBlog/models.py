
# Create your models here.
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
