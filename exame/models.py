
from django.db import models

class Exame(models.Model):

    cod_exame = models.CharField(max_length=10, primary_key=True)
    qtd_questoes = models.IntegerField()

    def __str__(self):
        return self.cod_exame

class Questao(models.Model):
    
    cod_exame = models.ForeignKey(Exame, on_delete=models.DO_NOTHING)
    pergunta = models.CharField('Pergunta', max_length=500)
    alternativa1 = models.CharField(max_length=500)
    alternativa2 = models.CharField(max_length=500)
    alternativa3 = models.CharField(max_length=500)
    alternativa4 = models.CharField(max_length=500)
    resposta = models.CharField(max_length=500)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.pergunta
