from django.contrib import admin
from api.models import models
from rangefilter.filters import DateRangeFilter
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
   
def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(models.Movimentacao)
class MovementAdmin(admin.ModelAdmin):
    list_display = [
        'get_description', 'get_tipo_movimentacao', 'get_category', 'get_payment_method', 'get_card',
        'get_account', 'get_status', 'get_expected_value', 'get_paid_value', 'data_vencimento', 'data_pagamento'
    ]

    list_filter = [
        'status_movimentacao__descricao', 'tipo_movimentacao__descricao', 'forma_pagamento__descricao', ('data_vencimento', DateRangeFilter), 
        'data_vencimento', ('conta_origem__descricao', custom_titled_filter('Conta origem')), 'centro_custo__descricao'
    ]

    ordering = ['data_vencimento', 'data_pagamento']

    search_fields = ['descricao', ]

    @admin.display(ordering='descricao', description='Tipo')
    def get_description(self, obj):
        
        if (obj.parcela_atual is not None and obj.parcela_atual > 0) and (obj.parcela_atual is not None and obj.parcela_total > 0):
            obj.descricao += ' - {}/{}'.format(obj.parcela_atual, obj.parcela_total)

        return obj.descricao

    @admin.display(ordering='tipo_movimentacao__descricao', description='Tipo')
    def get_tipo_movimentacao(self, obj):
        return obj.tipo_movimentacao.descricao

    @admin.display(ordering='categoria__descricao', description='Categoria')
    def get_category(self, obj):
        return obj.categoria.descricao

    @admin.display(ordering='forma_pagamento__descricao', description='Forma Pagamento')
    def get_payment_method(self, obj):
        if not obj.forma_pagamento:
            return None

        return obj.forma_pagamento.descricao

    @admin.display(ordering='cartao__descricao', description='Cartão')
    def get_card(self, obj):
        if not obj.cartao:
            return None

        return obj.cartao.bandeira.descricao

    @admin.display(ordering='conta_origem__descricao', description='Conta')
    def get_account(self, obj):
        if not obj.conta_origem:
            return None

        return obj.conta_origem.descricao

    @admin.display(ordering='parcela_atual', description='Parcela atual')
    def get_current_installment(self, obj):
        return obj.parcela_atual

    @admin.display(ordering='parcela_total', description='Parcela total')
    def get_total_installment(self, obj):
        return obj.parcela_total
    
    @admin.display(ordering='status_movimentacao__descricao', description='Status')
    def get_status(self, obj):
        return obj.status_movimentacao.descricao
    
    @admin.display(ordering='valor_previsao', description='Valor previsto')
    def get_expected_value(self, obj):
        if not obj.valor_previsao:
            return locale.currency(0, grouping=True)

        return locale.currency(obj.valor_previsao, grouping=True)

    @admin.display(ordering='valor_pago', description='Valor pago')
    def get_paid_value(self, obj):
        if not obj.valor_pago:
            return locale.currency(0, grouping=True)

        return locale.currency(obj.valor_pago, grouping=True)

    @admin.display(ordering='centro_custo__descricao', description='Centro Custo')
    def get_center_cost(self, obj):
        return obj.centro_custo.descricao

@admin.register(models.Cartao)
class CardAdmin(admin.ModelAdmin):
    list_display = ['get_brand', 'get_acount', 'valor_limite_total', 'dia_vencimento']
    search_fields = ['conta__descricao']

    @admin.display(ordering='bandeira__descricao', description='Bandeira')
    def get_brand(self, obj):
        return obj.bandeira.descricao

    @admin.display(ordering='conta__descricao', description='Conta')
    def get_acount(self, obj):
        return obj.conta.descricao


@admin.register(models.Fatura)
class FaturaAdmin(admin.ModelAdmin):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    list_display = [
        'get_card_brand', 'get_bank', 'data_vencimento', 'get_total_value',
        'get_paid_value', 'get_restant_value', 'get_total_limit', 'get_restant_limit',
        'get_status'
    ]

    list_filter = [
    ]

    ordering = ['data_vencimento']

    search_fields = ['descricao', ]
    
    @admin.display(ordering='cartao__bandeira__descricao', description='Bandeira')
    def get_card_brand(self, obj):
        return obj.cartao.bandeira.descricao

    @admin.display(ordering='instituicao_financeira__descricao', description='Banco')
    def get_bank(self, obj):
        return obj.instituicao_financeira.descricao

    @admin.display(ordering='valor_total', description='Valor total')
    def get_total_value(self, obj):
        if not obj.valor_total:
            return locale.currency(0, grouping=True)

        return locale.currency(obj.valor_total, grouping=True)

    @admin.display(ordering='valor_pago', description='Valor pago')
    def get_paid_value(self, obj):
        if not obj.valor_pago:
            return locale.currency(0, grouping=True)

        return locale.currency(obj.valor_pago, grouping=True)

    @admin.display(ordering='valor_restante', description='Valor restante')
    def get_restant_value(self, obj):
        valor_restante = obj.valor_total - obj.valor_pago

        return locale.currency(valor_restante, grouping=True)

    @admin.display(ordering='cartao__valor_limite_total', description='Limite total')
    def get_total_limit(self, obj):
        return locale.currency(obj.cartao.valor_limite_total, grouping=True)
    
    @admin.display(ordering='cartao__valor_limite_disponivel', description='Limite disponivel')
    def get_restant_limit(self, obj):
        return locale.currency(obj.cartao.valor_limite_disponivel, grouping=True)

    @admin.display(ordering='status__descricao', description='Status')
    def get_status(self, obj):
        return obj.status.descricao
