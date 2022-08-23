from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.generics import get_object_or_404

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import pagination


"""
API V1
"""

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    """
    1. caso o usuario passe o id de um curso especifico e avaliacoes,
       traga todas as avaliações deste curso
       referencia ao endpoint de: cursos/<int:curso_pk>/avaliacoes/

    2. se não, traga todas as avaliacoes de todos os cursos 
       endpoint de : cursos/
    """
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))

        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    """
    1. pegar uma avaliacao especifica de um curso especifico
       referente a url de: cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>
    
    2. pegando uma avaliacao especifica de avaliacoes 
       referente a url de: avaliacoes/<int:avaliacao_pk>

    3. url de: avaliacoes/ nos tras todas as avaliacoes
    """
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                    curso_id=self.kwargs.get('curso_pk'),
                                    pk=self.kwargs.get('avaliacao_pk'))          

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    """
    1. action criado para resolver url: api/v2/cursos/<int:curso_pk>/avaliacoes/
    2. modificando para tambem funcionar paginação em api/v2/cursos/<int:curso_pk>/avaliacoes/
    """

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        pagination.PageNumberPagination.get_page_size()
        
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

