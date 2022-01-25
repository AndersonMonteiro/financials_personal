from api.serializers.serializers import GrupoAcessoSerializer
from api.domain.services.grupo_acesso_service import GrupoAcessoService
from api.filters.filters import GrupoAcessoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters

class GrupoAcessoCreateList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = GrupoAcessoFilter
    search_fields = ['']

    def __init__(self):
        self.grupo_acesso_service = GrupoAcessoService()

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.grupo_acesso_service.consulta_grupo_acesso_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = GrupoAcessoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GrupoAcessoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        grupo_acesso = self.grupo_acesso_service.cria_grupo_acesso(request.data)

        return Response(grupo_acesso, status=status.HTTP_201_CREATED)

class GrupoAcessoUpdate(APIView):
    
    def __init__(self):
        self.grupo_acesso_service = GrupoAcessoService()

    def path(self, request, pk):
        serializer = GrupoAcessoSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        grupo_acesso_serialized = self.grupo_acesso_service.atualiza_grupo_acesso(
            pk, serializer.data)

        return Response(grupo_acesso_serialized, status=status.HTTP_201_CREATED)
