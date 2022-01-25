from api.serializers.serializers import CartaoSerializer
from api.domain.services.cartao_service import CartaoService
from api.filters.filters import CartaoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters import rest_framework as drf_filters
from rest_framework import filters


class CartaoCreateList(APIView):
    filter_backends = (drf_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = CartaoFilter
    search_fields = ['']

    def __init__(self):
        self.cartao_service = CartaoService()

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.cartao_service.consulta_cartao_todos()
        queryset_filtered = self.filter_queryset(queryset)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset_filtered, request)
        serializer = CartaoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartaoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cartao = self.cartao_service.cria_cartao(request.data)

        return Response(cartao, status=status.HTTP_201_CREATED)


class CartaoUpdateRetrieve(APIView):

    def __init__(self):
        self.cartao_service = CartaoService()

    def get(self, request, pk):
        cartao = self.cartao_service.consulta_cartao_por_id(pk)

        if cartao is None:
            return Response('error: cartão não encontrado.', status=status.HTTP_404_NOT_FOUND)

        serializer = CartaoSerializer(cartao)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def path(self, request, pk):
        serializer = CartaoSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cartao_serialized = self.cartao_service.atualiza_cartao(
            pk, serializer.data)

        return Response(cartao_serialized, status=status.HTTP_201_CREATED)
