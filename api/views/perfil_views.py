from api.serializers.serializers import PerfilSerializer
from api.domain.services.perfil_service import PerfilService
from api.filters.filters import PerfilFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters


class PerfilCreateListView(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_class = PerfilFilter

    def __init__(self):
        self.perfil_service = PerfilService()

    def post(self, request):
        serializer = PerfilSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized = self.perfil_service.cria_perfil(request.data)

        return Response(serialized, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.perfil_service.consulta_perfil_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = PerfilSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PerfilRetrieveUpdateView(APIView):
    def __init__(self):
        self.perfil_service = PerfilService()

    def patch(self, request, pk):
        serializer = PerfilSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized = self.perfil_service.atualiza_perfil(pk, serializer.data)

        return Response(serialized, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        perfil = self.perfil_service.consulta_perfil_por_id(pk)

        if perfil is None:
            return Response('error: perfil não encontrado.', status=status.HTTP_404_NOT_FOUND)

        serializer = PerfilSerializer(perfil)

        return Response(serializer.data, status=status.HTTP_200_OK)
