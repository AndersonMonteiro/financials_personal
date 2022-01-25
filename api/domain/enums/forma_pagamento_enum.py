from enum import IntEnum


class FormaPagamentoEnum(IntEnum):
    BOLETO = 1
    CARTAO_DEBITO = 2
    CARTAO_CREDITO = 3
    DINHEIRO = 4
    TRANSFERENCIA_BANCARIA = 5
    VOUCHER = 6
    DEBITO_AUTOMATICO = 7
