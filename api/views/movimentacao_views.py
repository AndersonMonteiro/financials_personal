from api.serializers.serializers import MovimentacaoSerializer
from api.domain.services.movimentacao_service import MovimentacaoService
from api.filters.filters import MovimentacaoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters

class MovimentacaoSheetList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = MovimentacaoFilter
    search_fields = ['descricao']
    
    def __init__(self):
        self.movimentacao_service = MovimentacaoService()

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.movimentacao_service.consulta_planilha()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = MovimentacaoSerializer(page, many=True)
        serializer = MovimentacaoSerializer(queryset, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

class MovimentacaoCreateList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = MovimentacaoFilter
    search_fields = ['descricao']

    def __init__(self):
        self.movimentacao_service = MovimentacaoService()

    def post(self, request):
        serializer = MovimentacaoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        movimentacao = self.movimentacao_service.cria_movimentacao(
            request.data)

        return Response(movimentacao, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.movimentacao_service.consulta_movimentacao_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = MovimentacaoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MovimentacaoUpdateRetrieve(APIView):

    def __init__(self):
        self.movimentacao_service = MovimentacaoService()

    def get(self, request, pk):
        movimentacao = self.movimentacao_service.consulta_movimentacao_por_id(
            pk)

        if movimentacao is None:
            return Response('error: movimentação não encontrado.', status=status.HTTP_404_NOT_FOUND)

        serializer = MovimentacaoSerializer(movimentacao)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        serializer = MovimentacaoSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        movimentacao_serialized = self.movimentacao_service.atualiza_movimentacao(
            pk, serializer.data)

        return Response(movimentacao_serialized, status=status.HTTP_201_CREATED)


class SyncMovimentacaoSheet(APIView):

    def post(self, request):
        MovimentacaoService().sincroniza_movimentacao_sheet()

        return Response('ok', status=status.HTTP_201_CREATED)
