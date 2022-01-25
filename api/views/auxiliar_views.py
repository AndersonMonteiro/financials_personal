
from api.serializers.serializers import (
    MoedaSerializer, TipoMovimentacaoSerializer, FormaPagamentoSerializer, StatusMovimentacaoSerializer,
    CategoriaSerializer, TipoContaSerializer, InstituicaoFinanceiraSerializer, BandeiraSerializer,
    PrioridadeMovimentacaoSerializer, TipoGrupoAcessoSerializer
)
from api.domain.services.auxiliar_service import (
    MoedaService, TipoMovimentacaoService, FormaPagamentoService, StatusMovimentacaoService,
    CategoriaService, TipoContaService, InstituicaoFinanceiraService, BandeiraService,
    PrioridadeMovimentacaoService, TipoGrupoAcessoService
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import filters


class BandeiraList(APIView):

    bandeira_service = BandeiraService()
    data = bandeira_service.consulta_bandeiras()

    filter_backends = (filters.SearchFilter,)
    search_fields = ['descricao']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return self.data

    def get(self, request):
        paginator = PageNumberPagination()

        data = self.filter_queryset(self.get_queryset())
        page = paginator.paginate_queryset(data, request)

        serializer = BandeiraSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriaList(APIView):

    def get(self, request):
        categoria_service = CategoriaService()
        data = categoria_service.consulta_categorias()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = CategoriaSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FormaPagamentoList(APIView):

    def get(self, request):
        forma_pagamento_service = FormaPagamentoService()
        data = forma_pagamento_service.consulta_formas_pagamento()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = FormaPagamentoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class InstituicaoFinanceiraList(APIView):

    instituicao_financeira_service = InstituicaoFinanceiraService()
    data = instituicao_financeira_service.consulta_instituicoes_financeiras()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['descricao', 'codigo', 'nome_completo']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return self.data

    def get(self, request):
        paginator = PageNumberPagination()

        data = self.filter_queryset(self.get_queryset())
        page = paginator.paginate_queryset(data, request)

        serializer = InstituicaoFinanceiraSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoedaList(APIView):
    """
    Consulta Lista de Moedas

    Serviço utilizado para consulta das possíveis soluções de captura
    """

    def get(self, request):
        moeda_service = MoedaService()
        data = moeda_service.consulta_moedas()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = MoedaSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PrioridadeMovimentacaoList(APIView):

    def get(self, request):
        prioridade_movimentacao_service = PrioridadeMovimentacaoService()
        data = prioridade_movimentacao_service.consulta_prioridades_movimentacao()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = PrioridadeMovimentacaoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusMovimentacaoList(APIView):

    def get(self, request):
        status_movimentacao_service = StatusMovimentacaoService()
        data = status_movimentacao_service.consulta_status_movimentacao()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = StatusMovimentacaoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TipoMovimentacaoList(APIView):

    def get(self, request):
        tipo_movimentacao_service = TipoMovimentacaoService()
        data = tipo_movimentacao_service.consulta_tipos_movimentacao()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = TipoMovimentacaoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TipoContaList(APIView):

    def get(self, request):
        tipo_conta_service = TipoContaService()
        data = tipo_conta_service.consulta_tipos_conta()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = TipoContaSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

class TipoGrupoAcessoList(APIView):
    
    def get(self, request):
        tipo_grupo_acesso_service = TipoGrupoAcessoService()
        data = tipo_grupo_acesso_service.consulta_tipos_grupos_acesso()

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = TipoGrupoAcessoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
