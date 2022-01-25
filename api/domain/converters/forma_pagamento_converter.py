from api.domain.enums.forma_pagamento_enum import FormaPagamentoEnum

class FormaPagamentoSwitch:

    def convert_from_sheet(self, var):
        return {
            'Boleto': int(FormaPagamentoEnum.BOLETO),
            'Cartão de débito': int(FormaPagamentoEnum.CARTAO_DEBITO),
            'Cartão de crédito': int(FormaPagamentoEnum.CARTAO_CREDITO),
            'Dinheiro': int(FormaPagamentoEnum.DINHEIRO),
            'Transferência bancária': int(FormaPagamentoEnum.TRANSFERENCIA_BANCARIA),
            'Voucher': int(FormaPagamentoEnum.VOUCHER),
            'Débito automático': int(FormaPagamentoEnum.DEBITO_AUTOMATICO)
        }.get(var, False)
