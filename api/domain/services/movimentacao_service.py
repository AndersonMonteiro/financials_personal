from api.domain.entities.movimentacao_entity import MovimentacaoEntity
from api.domain.repositories.movimentacao_repository import MovimentacaoRepository
from api.domain.enums.status_movimentacao_enum import StatusMovimentacaoEnum
from api.domain.clients.movimentacao_sheet_client import MovimentacaoSheetClient
from datetime import datetime


class MovimentacaoService:
    def __init__(self):
        self.movimentacao_repository = MovimentacaoRepository()

    def cria_movimentacao(self, movimentacao):
        movimentacao['data_cadastro'] = datetime.now()
        movimentacao['status_movimentacao'] = int(StatusMovimentacaoEnum.AGUARDANDO)
        movimentacao = self.movimentacao_repository.cria_movimentacao(movimentacao)

        return movimentacao

    def cria_movimentacao_bulk(self, movimentacoes):
        self.movimentacao_repository.cria_movimentacao_bulk(movimentacoes)

        return None

    def atualiza_movimentacao(self, movimentacao_id, movimentacao):
        movimentacao['data_atualizacao'] = datetime.now()
        movimentacao = self.movimentacao_repository.atualiza_movimentacao(movimentacao_id, movimentacao)

        return movimentacao

    def consulta_movimentacao_todos(self):
        movimentacoes = self.movimentacao_repository.consulta_movimentacao_todos()

        return movimentacoes

    def consulta_movimentacao_por_id(self, movimentacao_id):
        movimentacao = self.movimentacao_repository.consulta_movimentacao_por_id(movimentacao_id)

        return movimentacao

    def sincroniza_movimentacao_sheet(self):
        movimentacoes_sheet = MovimentacaoSheetClient().consulta_movimentacoes()
        movimentacoes_planilha = []
        movimentacoes_indexadas = self.consulta_movimentacao_todos()

        for mov in movimentacoes_sheet:
            if mov['id']:
                movimentacao_normalizada = MovimentacaoEntity().create_from_movimentacao_sheet(mov)
                movimentacoes_planilha.append(movimentacao_normalizada)

        checkables_fields = [
            f for f in movimentacoes_planilha[0]._meta.fields if f.name not in ['data_cadastro', 'data_atualizacao', 'id']
        ]

        movimentacao_planilha_existentes = [
            m for m in movimentacoes_planilha if m.movimentacao_sheet_id in [
                me.movimentacao_sheet_id for me in movimentacoes_indexadas
            ]
        ]

        movimentacao_novos = [
            m for m in movimentacoes_planilha if m.movimentacao_sheet_id not in [
                me.movimentacao_sheet_id for me in movimentacoes_indexadas
            ]
        ]

        movimentacao_removidos = [
            m for m in movimentacoes_indexadas if m.movimentacao_sheet_id not in [
                mp.movimentacao_sheet_id for mp in movimentacoes_planilha
            ]
        ]

        if movimentacao_planilha_existentes:
            for mov in movimentacao_planilha_existentes:
                print('Proccessing {}/{}'.format(
                    list(movimentacoes_planilha).index(mov) + 1, len(list(movimentacoes_planilha))
                ))

                movimentacao_indexada = [m for m in movimentacoes_indexadas if mov.movimentacao_sheet_id == m.movimentacao_sheet_id][0]

                field_to_update = []

                for field in checkables_fields:

                    field_movimentacao_indexada = getattr(movimentacao_indexada, field.name)
                    field_movimentacao_planilha = getattr(mov, field.name)

                    if field_movimentacao_indexada != field_movimentacao_planilha:
                        setattr(movimentacao_indexada, field.name, field_movimentacao_planilha)
                        field_to_update.append(field.name)

                if field_to_update:
                    movimentacao_indexada.save(update_fields=field_to_update)

        if movimentacao_novos:
            self.cria_movimentacao_bulk(movimentacao_novos)

        for mov_rem in movimentacao_removidos:
            mov_rem.status_ativo = False
            mov_rem.save()

    def consulta_planilha(self):
        movimentacoes_sheet = MovimentacaoSheetClient().consulta_movimentacoes()

        movimentacoes = []

        for mov in movimentacoes_sheet:
            if mov['id']:
                movimentacao = MovimentacaoEntity().create_from_movimentacao_sheet(mov)
                movimentacoes.append(movimentacao)

        return movimentacoes
