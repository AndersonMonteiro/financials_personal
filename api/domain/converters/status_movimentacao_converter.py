from api.domain.enums.status_movimentacao_enum import StatusMovimentacaoEnum


class StatusMovimentacaoSwitch:

    def convert_from_sheet(self, var):
        return {
            'Aguardando': int(StatusMovimentacaoEnum.AGUARDANDO),
            'Pago': int(StatusMovimentacaoEnum.PAGO),
            'Pendente': int(StatusMovimentacaoEnum.PENDENTE),
            'Cancelado': int(StatusMovimentacaoEnum.CANCELADO),
            'Parcialmente efetivada': int(StatusMovimentacaoEnum.PARCIALMENTE_PAGO)
        }.get(var, False)
