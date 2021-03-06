from api.models.models import Movimentacao, Categoria
from api.domain.enums.tipo_movimentacao_enum import TipoMovimentacaoEnum
from api.domain.enums.categoria_enum import CategoriaEnum
from api.domain.enums.moeda_enum import MoedaEnum
from api.domain.converters.categoria_converter import CategoriaSwitch
from api.domain.converters.tipo_movimentacao_converter import TipoMovimentacaoSwitch
from api.domain.converters.status_movimentacao_converter import StatusMovimentacaoSwitch
from api.domain.converters.forma_pagamento_converter import FormaPagamentoSwitch
from api.domain.converters.cartao_converter import CartaoSwitch
from api.domain.converters.centro_custo_converter import CentroCustoEnum, CentroCustoSwitch
import uuid
import datetime


class MovimentacaoEntity:

    def create_from_movimentacao_sheet(self, movimentacao_sheet):
        categoria_id = CategoriaSwitch().convert_from_sheet(movimentacao_sheet['categoria'])
        tipo_movimentacao_id = TipoMovimentacaoSwitch().convert_from_sheet(movimentacao_sheet['tipo_movimentacao'])
        status_id = StatusMovimentacaoSwitch().convert_from_sheet(movimentacao_sheet['status'])
        forma_pagamento_id = FormaPagamentoSwitch().convert_from_sheet(movimentacao_sheet['forma_pagamento'])
        cartao_id = CartaoSwitch().convert_from_sheet(movimentacao_sheet['cartao'])
        centro_custo_id = CentroCustoSwitch().convert_from_sheet(movimentacao_sheet['centro_custo'])

        movimentacao = Movimentacao(
            descricao=movimentacao_sheet['descricao'],
            tipo_movimentacao_id=tipo_movimentacao_id,
            status_movimentacao_id=status_id,
            data_cadastro=datetime.datetime.now(),
            categoria_id=categoria_id,
            moeda_id=int(MoedaEnum.REAL),
            movimentacao_sheet_id=uuid.UUID(movimentacao_sheet['id']),
            forma_pagamento_id=forma_pagamento_id,
            centro_custo_id=centro_custo_id
        )
        
        if cartao_id and cartao_id > 0:
            movimentacao.cartao_id = cartao_id
            movimentacao.conta_origem_id = movimentacao.cartao.conta_id

        if movimentacao_sheet['data_realizacao']:
            movimentacao.data_realizacao = datetime.datetime.strptime(movimentacao_sheet['data_realizacao'], '%d/%m/%Y').date()

        if movimentacao_sheet['data_vencimento']:
            movimentacao.data_vencimento = datetime.datetime.strptime(movimentacao_sheet['data_vencimento'], '%d/%m/%Y').date()

        if movimentacao_sheet['data_pagamento']:
            movimentacao.data_pagamento = datetime.datetime.strptime(movimentacao_sheet['data_pagamento'], '%d/%m/%Y').date()

        if movimentacao_sheet['parcela_atual'] and isinstance(movimentacao_sheet['parcela_atual'], int):
            movimentacao.parcela_atual = movimentacao_sheet['parcela_atual']

        if movimentacao_sheet['parcela_final'] and isinstance(movimentacao_sheet['parcela_final'], int):
            movimentacao.parcela_total = movimentacao_sheet['parcela_final']

        if movimentacao_sheet['valor_previsao']:
            valor_previsao = str(movimentacao_sheet['valor_previsao']).replace('.', '')
            valor_previsao = valor_previsao.replace('R$ ', '')
            movimentacao.valor_previsao = float(valor_previsao.replace(',', '.'))

        if movimentacao_sheet['valor_processado']:
            valor_processado = str(movimentacao_sheet['valor_processado']).replace('.', '')
            valor_processado = valor_processado.replace('R$ ', '')
            movimentacao.valor_pago = float(valor_processado.replace(',', '.'))

        return movimentacao
