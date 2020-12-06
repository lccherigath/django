from rest_framework import viewsets
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    '''
    A simple ViewSet for viewing and editing accounts
    '''
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # filter_fields = ('nome', 'descricao',)
    filterset_fields = ['nome', 'descricao']