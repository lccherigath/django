from rest_framework import viewsets
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    '''
    A simple ViewSet for viewing and editing accounts
    '''
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
