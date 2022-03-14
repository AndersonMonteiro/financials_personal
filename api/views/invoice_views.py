from api.serializers.serializers import FaturaSerializer
from api.domain.services.fatura_service import FaturaService
from api.filters.filters import FaturaFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters


class InvoiceCreateList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = FaturaFilter
    search_fields = ['']

    def __init__(self):
        self.fatura_service = FaturaService()

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.fatura_service.consulta_fatura_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = FaturaSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FaturaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        fatura = self.fatura_service.cria_fatura(request.data)

        return Response(fatura, status=status.HTTP_201_CREATED)


class InvoiceUpdateRetrieve(APIView):

    def __init__(self):
        self.fatura_service = FaturaService()

    def get(self, request, pk):
        fatura = self.fatura_service.consulta_fatura_por_id(pk)

        if fatura is None:
            return Response('error: fatura não encontrada.', status=status.HTTP_404_NOT_FOUND)

        serializer = FaturaSerializer(fatura)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def path(self, request, pk):
        serializer = FaturaSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        fatura_serialized = self.fatura_service.atualiza_fatura(
            pk, serializer.data)

        return Response(fatura_serialized, status=status.HTTP_201_CREATED)
