from api.domain.enums.forma_pagamento_enum import FormaPagamentoEnum


class StatusMovimentacaoSwitch:

    def convert_from_sheet(self, var):
        var_normalized = str(var).lower()

        return {
            'boleto': int(FormaPagamentoEnum.BOLETO),
            'cartão de débito': int(FormaPagamentoEnum.CARTAO_DEBITO),
            'cartão de crédito': int(FormaPagamentoEnum.CARTAO_CREDITO),
            'dinheiro': int(FormaPagamentoEnum.DINHEIRO),
            'transferência bancária': int(FormaPagamentoEnum.TRANSFERENCIA_BANCARIA),
            'voucher': int(FormaPagamentoEnum.VOUCHER),
            'débito automático': int(FormaPagamentoEnum.DEBITO_AUTOMATICO)
        }.get(var_normalized, False)
