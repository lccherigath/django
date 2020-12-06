from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def campo_adicional_2(self):
        """
        Campo com informações adicionais (aula 33)
        """
        return f"CAMPO ADICIONAL 2 ### {self.nome} ### {'Aprovado' if self.aprovado else 'Reprovado'}"


    def __str__(self):
        return self.nome
