from api.domain.providers.movimentacao_sheet_provider import MovimentacaoSheetProvider

class MovimentacaoSheetClient:

    def consulta_movimentacoes(self):
        movimentacoes = MovimentacaoSheetProvider().consulta_movimentacoes()

        return movimentacoes
