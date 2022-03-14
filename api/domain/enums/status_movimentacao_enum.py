from enum import IntEnum


class StatusMovimentacaoEnum(IntEnum):
    AGUARDANDO = 1
    PAGO = 2
    PENDENTE = 3
    CANCELADO = 4
    PARCIALMENTE_PAGO = 5
