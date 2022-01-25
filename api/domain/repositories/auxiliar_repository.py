from api.models.models import (
    Moeda, TipoMovimentacao, FormaPagamento, StatusMovimentacao, Categoria,
    TipoConta, InstituicaoFinanceira, Bandeira, PrioridadeMovimentacao,
    TipoGrupoAcesso
)

class MoedaRepository:
    def consulta_moedas(self):
        queryset = Moeda.objects.all()

        return queryset


class TipoMovimentacaoRepository:
    def consulta_tipos_movimentacao(self):
        queryset = TipoMovimentacao.objects.all()

        return queryset


class FormaPagamentoRepository:
    def consulta_formas_pagamento(self):
        queryset = FormaPagamento.objects.all()

        return queryset


class StatusMovimentacaoRepository:
    def consulta_status_movimentacao(self):
        queryset = StatusMovimentacao.objects.all()

        return queryset


class PrioridadeMovimentacaoRepository:
    def consulta_prioridades_movimentacao(self):
        queryset = PrioridadeMovimentacao.objects.all()

        return queryset


class TipoContaRepository:
    def consulta_tipos_conta(self):
        queryset = TipoConta.objects.all()

        return queryset


class InstituicaoFinanceiraRepository:
    def consulta_instituicoes_financeiras(self):
        queryset = InstituicaoFinanceira.objects.all()

        return queryset


class BandeiraRepository:
    def consulta_bandeiras(self):
        queryset = Bandeira.objects.all()

        return queryset


class CategoriaRepository:
    def consulta_categorias(self):
        queryset = Categoria.objects.all()

        return queryset

class TipoGrupoAcessoRepository:
    def consulta_tipos_grupos_acesso(self):
        queryset = TipoGrupoAcesso.objects.all()

        return queryset
