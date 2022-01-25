from enum import IntEnum


class StatusMovimentacaoEnum(IntEnum):
    AGUARDANDO = 1
    EFETIVADA = 2
    PENDENTE = 3
    CANCELADO = 4
    PARCIALMENTE_EFETIVADA = 5
