from api.serializers.serializers import ContaSerializer
from api.domain.services.conta_service import ContaService
from api.filters.filters import ContaFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters


class ContaCreateList(APIView):

    conta_service = ContaService()
    queryset = conta_service.consulta_contas()

    filter_backends = (filters.SearchFilter, drf_filters.DjangoFilterBackend,)
    search_fields = ['codigo_conta', 'codigo_agencia']
    filterset_class = ContaFilter

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return self.queryset

    def get(self, request):
        paginator = PageNumberPagination()

        queryset = self.filter_queryset(self.get_queryset())
        page = paginator.paginate_queryset(queryset, request)

        serializer = ContaSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        conta = self.conta_service.cria_conta(request.data)

        return Response(conta, status=status.HTTP_201_CREATED)


class ContaUpdateRetrieve(APIView):

    def __init__(self):
        self.conta_service = ContaService()

    def get(self, request, pk):
        conta = self.conta_service.consulta_conta_por_id(pk)

        if conta is None:
            return Response('error: conta não encontrada.', status=status.HTTP_404_NOT_FOUND)

        serializer = ContaSerializer(conta)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        serializer = ContaSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized = self.conta_service.atualiza_conta(pk, request.data)

        return Response(serialized, status=status.HTTP_201_CREATED)
