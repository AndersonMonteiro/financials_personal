from api.models.models import Movimentacao, Categoria
from api.domain.enums.tipo_movimentacao_enum import TipoMovimentacaoEnum
from api.domain.enums.categoria_enum import CategoriaEnum
from api.domain.enums.moeda_enum import MoedaEnum
from api.domain.converters.categoria_converter import CategoriaSwitch
from api.domain.converters.tipo_movimentacao_converter import TipoMovimentacaoSwitch
from api.domain.converters.status_movimentacao_converter import StatusMovimentacaoSwitch
import uuid
import unicodedata
import datetime


class MovimentacaoEntity:

    def create_from_movimentacao_sheet(self, movimentacao_sheet):
        categoria_id = CategoriaSwitch().convert_from_sheet(movimentacao_sheet['categoria'])
        tipo_movimentacao_id = TipoMovimentacaoSwitch().convert_from_sheet(movimentacao_sheet['tipo_movimentacao'])
        status_id = StatusMovimentacaoSwitch().convert_from_sheet(movimentacao_sheet['status'])

        movimentacao = Movimentacao(
            descricao=movimentacao_sheet['descricao'],
            tipo_movimentacao_id=tipo_movimentacao_id,
            status_movimentacao_id=status_id,
            data_cadastro=datetime.datetime.now(),
            categoria_id=categoria_id,
            moeda_id=int(MoedaEnum.REAL),
            movimentacao_sheet_id=uuid.UUID(movimentacao_sheet['id'])
        )

        if movimentacao_sheet['data_realizacao']:
            movimentacao.data_realizacao = datetime.datetime.strptime(movimentacao_sheet['data_realizacao'], '%d/%m/%Y').date()

        if movimentacao_sheet['data_vencimento']:
            movimentacao.data_vencimento = datetime.datetime.strptime(movimentacao_sheet['data_vencimento'], '%d/%m/%Y').date()

        if movimentacao_sheet['data_pagamento']:
            movimentacao.data_pagamento = datetime.datetime.strptime(movimentacao_sheet['data_pagamento'], '%d/%m/%Y').date()

        if movimentacao_sheet['parcela_atual'] and isinstance(movimentacao_sheet['parcela_atual'], int):
            movimentacao.parcela_atual = movimentacao_sheet['parcela_atual']

        if movimentacao_sheet['parcela_final'] and isinstance(movimentacao_sheet['parcela_final'], int):
            movimentacao.parcela_final = movimentacao_sheet['parcela_final']

        if movimentacao_sheet['valor_previsao']:
            valor_previsao = str(movimentacao_sheet['valor_previsao']).replace('.', '')
            valor_previsao = valor_previsao.replace('R$ ', '')
            movimentacao.valor_previsao = float(valor_previsao.replace(',', '.'))

        if movimentacao_sheet['valor_processado']:
            valor_processado = str(movimentacao_sheet['valor_processado']).replace('.', '')
            valor_processado = valor_processado.replace('R$ ', '')
            movimentacao.valor_pago = float(valor_processado.replace(',', '.'))

        return movimentacao
