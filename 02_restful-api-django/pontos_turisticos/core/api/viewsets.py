from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.http import HttpResponse

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    '''
    A simple ViewSet for viewing and editing accounts
    '''
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    ### Buscas com SearchFilter (aula 27)
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    # lookup_field = 'field'  ### Substitui o campo de busca padrão (id) por outro campo único (aula 28)

    ### Autenticação e Autorização
    # authentication_classes = [TokenAuthentication]
    # # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly] ### Só permite a execução de métodos http seguros (GET, HEAD ou OPTIONS)

    def get_queryset(self):
        """
        Determina a lista de objetos que se deseja exibir.
        Por padrão, fornecerá todos os registros especificados pelo modelo.
        Ao substituir essa função, pode-se estender ou substituir completamente essa lógica.
        (remover o queryset e inserir basename em router.register)
        """
        # return PontoTuristico.objects.filter(aprovado=True)

        ### Filtragem por query params (aula 25)
        # id = self.request.query_params['id']
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Sobrescrevendo GET de listagem
        """
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Sobrescrevendo POST
        """
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        """
        Action personalizada
        """
        print('pk', pk)
        return Response({'action': 'denunciar'})

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        """
        Action personalizada para relacionamento com chaves estrangeiras já existentes no banco
        """
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('Ok')

    # def list(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo GET de listagem
    #     """
    #     return Response({'get': 'list'})

    # def create(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo POST
    #     """
    #     print('data', request.data)
    #     # print(f"{request.data['nome']}, {request.data['descricao']}, {request.data['aprovado']}")
    #     return Response({'post': 'create'})

    # def destroy(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo DELETE
    #     """
    #     print('pk', kwargs['pk'])
    #     return Response({'delete': 'destroy'})

    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo GET de registro
    #     """
    #     print('pk', kwargs['pk'])
    #     return Response({'get': 'retrieve'})

    # def update(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo PUT
    #     """
    #     print('pk', kwargs['pk'])
    #     print('data', request.data)
    #     return Response({'put': 'update'})

    # def partial_update(self, request, *args, **kwargs):
    #     """
    #     Sobrescrevendo PATCH
    #     """
    #     print('pk', kwargs['pk'])
    #     print('data', request.data)
    #     return Response({'patch': 'partial_update'})

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     """
    #     Action personalizada
    #     """
    #     print('pk', pk)
    #     return Response({'action': 'denunciar'})
