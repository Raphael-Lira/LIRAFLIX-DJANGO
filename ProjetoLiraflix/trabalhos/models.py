from django.db import models
from django.utils import timezone
# Create your models here.

class Trabalho(models.Model):
    #Criação de modelos para colocar infos no seu site
       #titulo / #thumb # descricção / categoria / data de criacao
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_trabalhos')
    descricao = models.TextField(max_length=1000)
    data_criacao = models.DateTimeField(default=timezone.now)
    # Retornando pra ficar com o nome certo na admin configs

    def __str__(self):
        return self.titulo