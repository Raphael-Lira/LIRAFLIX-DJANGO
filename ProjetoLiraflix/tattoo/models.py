from django.db import models
from django.utils import timezone
# Create your models here.
# Lista para dar multiplas categorias nesse formato

LISTA_CATEGORIAS = (
    ('LIMPOS', 'Limpos'),
    ('COBERTURAS', 'Coberturas'),
    ('FINEART', 'Fine Art'),
    ('OUTROS', 'Outros'),
)

class Tattoo(models.Model):
    #Criação de modelos para colocar infos no seu site
       #titulo / #thumb # descricção / categoria / data de criacao
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_tattos')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    data_criacao = models.DateTimeField(default=timezone.now)
    # Retornando pra ficar com o nome certo na admin configs
    def __str__(self):
        return self.titulo