from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco
# from comentarios.api.serializers import ComentarioSerializer
# from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # endereco = EnderecoSerializer(read_only=True) ### read_only permite criar recurso sem este campo
    endereco = EnderecoSerializer()
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    # comentarios = ComentarioSerializer(many=True, read_only=True)
    campo_adicional = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'endereco',
            # 'comentarios', 'avaliacoes',
            'campo_adicional',     # criado com SerializerMethodField
            'campo_adicional_2',   # criado com property()
            'doc_identificacao'
        )
        read_only_fields = ('comentarios', 'avaliacoes',)

    def create(self, validated_data):
        """
        Função personalizada para criação do recurso, que recebe dados de relacionamentos
        """
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']

        # Cria ponto turístico
        ponto = PontoTuristico.objects.create(**validated_data)
        # Cria relacionamentos n-n
        self.cria_atracoes(atracoes, ponto)
        # Cria relacionamento 1-n
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        # Cria relacionamento 1-n
        doc_i = DocIdentificacao.objects.create(**doc)
        ponto.doc_identificacao = doc_i

        ponto.save()

        return ponto
    
    def cria_atracoes(self, atracoes, ponto):
        """
        Cria relacionamentos N-N
        """
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def get_campo_adicional(self, obj):
        """
        Campo com informações adicionais (aula 33)
        """
        return f"CAMPO ADICIONAL 1 ### {obj.nome} ### {'Aprovado' if obj.aprovado else 'Reprovado'}"
