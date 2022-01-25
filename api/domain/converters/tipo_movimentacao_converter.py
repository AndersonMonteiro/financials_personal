from api.domain.enums.tipo_movimentacao_enum import TipoMovimentacaoEnum

class TipoMovimentacaoSwitch:

    def convert_from_sheet(self, var):
        return {
            'Despesa': int(TipoMovimentacaoEnum.DESPESA),
            'Receita': int(TipoMovimentacaoEnum.RECEITA)
        }.get(var, False)
