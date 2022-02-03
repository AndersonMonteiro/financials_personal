from api.serializers.serializers import ComentarioSerializer
from api.domain.services.comentario_service import ComentarioService
from api.filters.filters import ComentarioFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters


class CommentCreateList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = ComentarioFilter
    search_fields = ['']

    def __init__(self):
        self.comentario_service = ComentarioService()

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.comentario_service.consulta_comentario_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = ComentarioSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        comentario = self.comentario_service.cria_comentario(request.data)

        return Response(comentario, status=status.HTTP_201_CREATED)


class CommentUpdateRetrieve(APIView):

    def __init__(self):
        self.comentario_service = ComentarioService()

    def get(self, request, pk):
        comentario = self.comentario_service.consulta_comentario_por_id(pk)

        if comentario is None:
            return Response('error: comentário não encontrado.', status=status.HTTP_404_NOT_FOUND)

        serializer = ComentarioSerializer(comentario)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def path(self, request, pk):
        serializer = ComentarioSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        comentario_serialized = self.comentario_service.atualiza_comentario(
            pk, serializer.data)

        return Response(comentario_serialized, status=status.HTTP_201_CREATED)
