from api.domain.repositories.auxiliar_repository import (
    MoedaRepository, TipoMovimentacaoRepository, FormaPagamentoRepository, StatusMovimentacaoRepository,
    PrioridadeMovimentacaoRepository, TipoContaRepository, CategoriaRepository, InstituicaoFinanceiraRepository,
    BandeiraRepository, TipoGrupoAcessoRepository
    )


class MoedaService:
    def consulta_moedas(self):
        moeda_repository = MoedaRepository()
        queryset = moeda_repository.consulta_moedas()

        return queryset


class TipoMovimentacaoService:
    def consulta_tipos_movimentacao(self):
        tipo_movimentacao_repository = TipoMovimentacaoRepository()
        queryset = tipo_movimentacao_repository.consulta_tipos_movimentacao()

        return queryset


class FormaPagamentoService:
    def consulta_formas_pagamento(self):
        forma_pagamento_repository = FormaPagamentoRepository()
        queryset = forma_pagamento_repository.consulta_formas_pagamento()

        return queryset


class StatusMovimentacaoService:
    def consulta_status_movimentacao(self):
        status_movimentacao_repository = StatusMovimentacaoRepository()
        queryset = status_movimentacao_repository.consulta_status_movimentacao()

        return queryset


class PrioridadeMovimentacaoService:
    def consulta_prioridades_movimentacao(self):
        prioridade_movimentacao_repository = PrioridadeMovimentacaoRepository()
        queryset = prioridade_movimentacao_repository.consulta_prioridades_movimentacao()

        return queryset


class TipoContaService:
    def consulta_tipos_conta(self):
        tipos_conta_repository = TipoContaRepository()
        queryset = tipos_conta_repository.consulta_tipos_conta()

        return queryset


class CategoriaService:
    def consulta_categorias(self):
        categoria_repository = CategoriaRepository()
        queryset = categoria_repository.consulta_categorias()

        return queryset


class InstituicaoFinanceiraService:
    def consulta_instituicoes_financeiras(self):
        instituicao_financeira_repository = InstituicaoFinanceiraRepository()
        queryset = instituicao_financeira_repository.consulta_instituicoes_financeiras()

        return queryset


class BandeiraService:
    def consulta_bandeiras(self):
        bandeira_repository = BandeiraRepository()
        queryset = bandeira_repository.consulta_bandeiras()

        return queryset

class TipoGrupoAcessoService:
    def consulta_tipos_grupos_acesso(self):
        tipo_grupo_acesso_repository = TipoGrupoAcessoRepository()
        queryset = tipo_grupo_acesso_repository.consulta_tipos_grupos_acesso()

        return queryset
