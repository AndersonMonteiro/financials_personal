from api.models.models import (
    Conta, Endereco, Movimentacao, Perfil, Cartao, Comentario,
    GrupoAcesso
)
from django_filters import rest_framework as filtersdrf
import django_filters


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class TextInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass

class ContaFilter(django_filters.FilterSet):
    codigo_conta = django_filters.CharFilter(lookup_expr='icontains')
    codigo_agencia = django_filters.CharFilter(lookup_expr='icontains')
    tipo_conta = NumberInFilter(field_name='id_lote', lookup_expr='in')
    instituicao_financeira = NumberInFilter(field_name='id_lote', lookup_expr='in')
    data_cadastro_inicial = django_filters.DateTimeFilter(field_name='data_cadastro', lookup_expr='gte')
    data_cadastro_final = django_filters.DateTimeFilter(field_name='data_cadastro', lookup_expr='lte')
    data_atualizacao_inicial = django_filters.DateTimeFilter(field_name='data_atualizacao', lookup_expr='gte')
    data_atualizacao_final = django_filters.DateTimeFilter(field_name='data_atualizacao', lookup_expr='lte')

    class Meta:
        model = Conta
        fields = []

class EnderecoFilter(django_filters.FilterSet):

    class Meta:
        model = Endereco
        fields = []

class MovimentacaoFilter(django_filters.FilterSet):
    valor_devido_inicial = django_filters.NumberFilter(field_name='valor_devido', lookup_expr='gte')
    valor_devido_final = django_filters.NumberFilter(field_name='valor_devido', lookup_expr='lte')
    data_realizacao_inicial = django_filters.DateTimeFilter(field_name='data_realizacao', lookup_expr='gte')
    data_realizacao_final = django_filters.DateTimeFilter(field_name='data_realizacao', lookup_expr='lte')
    data_vencimento_inicial = django_filters.DateTimeFilter(field_name='data_vencimento', lookup_expr='gte')
    data_vencimento_final = django_filters.DateTimeFilter(field_name='data_vencimento', lookup_expr='lte')
    data_pagamento_inicial = django_filters.DateTimeFilter(field_name='data_pagamento', lookup_expr='gte')
    data_pagamento_final = django_filters.DateTimeFilter(field_name='data_pagamento', lookup_expr='lte')    
    data_cadastro_inicial = django_filters.DateTimeFilter(field_name='data_cadastro', lookup_expr='gte')
    data_cadastro_final = django_filters.DateTimeFilter(field_name='data_cadastro', lookup_expr='lte')
    data_atualizacao_inicial = django_filters.DateTimeFilter(field_name='data_atualizacao', lookup_expr='gte')
    data_atualizacao_final = django_filters.DateTimeFilter(field_name='data_atualizacao', lookup_expr='lte')
    tipo_movimentacao = NumberInFilter(field_name='tipo_movimentacao_id', lookup_expr='in')
    status_movimentacao = NumberInFilter(field_name='status_movimentacao_id', lookup_expr='in')
    prioridade = NumberInFilter(field_name='prioridade_id', lookup_expr='in')
    categoria = NumberInFilter(field_name='categoria_id', lookup_expr='in')
    perfil_responsavel = NumberInFilter(field_name='perfil_responsavel_id', lookup_expr='in')
    perfil_destinatario = NumberInFilter(field_name='perfil_destinatario_id', lookup_expr='in')
    forma_pagamento = NumberInFilter(field_name='forma_pagamento_id', lookup_expr='in')
    conta_origem = NumberInFilter(field_name='conta_origem_id', lookup_expr='in')
    conta_destino = NumberInFilter(field_name='conta_destino_id', lookup_expr='in')
    cartao = NumberInFilter(field_name='cartao_id', lookup_expr='in')

    class Meta:
        model = Movimentacao
        fields = []

class PerfilFilter(django_filters.FilterSet):

    class Meta:
        model = Perfil
        fields = []

class CartaoFilter(django_filters.FilterSet):

    class Meta:
        model = Cartao
        fields = []

class ComentarioFilter(django_filters.FilterSet):

    class Meta:
        model = Comentario
        fields = []

class GrupoAcessoFilter(django_filters.FilterSet):

    class Meta:
        model = GrupoAcesso
        fields = []
