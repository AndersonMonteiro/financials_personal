from api.serializers.serializers import EnderecoSerializer
from api.domain.services.endereco_service import EnderecoService
from api.filters.filters import EnderecoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters


class EnderecoCreateListView(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_class = EnderecoFilter

    def __init__(self):
        self.endereco_service = EnderecoService()

    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized = self.endereco_service.cria_endereco(request.data)

        return Response(serialized, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.endereco_service.consulta_endereco_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = EnderecoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EnderecoRetrievelUpdateView(APIView):

    def __init__(self):
        self.endereco_service = EnderecoService()

    def patch(self, request, pk):
        serializer = EnderecoSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        endereco_serialized = self.endereco_service.atualiza_endereco(
            pk, serializer.data)

        return Response(endereco_serialized, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        endereco = self.endereco_service.consulta_endereco_por_id(pk)

        if endereco is None:
            return Response('error: endereco não encontrado.', status=status.HTTP_404_NOT_FOUND)

        serializer = EnderecoSerializer(endereco)

        return Response(serializer.data, status=status.HTTP_200_OK)
