from rest_framework import viewsets
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    '''
    A simple ViewSet for viewing and editing accounts
    '''
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
