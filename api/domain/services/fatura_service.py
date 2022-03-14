from api.domain.repositories.fatura_repository import FaturaRepository
from datetime import datetime


class FaturaService:
    def __init__(self):
        self.fatura_repository = FaturaRepository()

    def cria_fatura(self, fatura):
        fatura['data_cadastro'] = datetime.now()
        fatura = self.fatura_repository.cria_fatura(fatura)

        return fatura

    def atualiza_fatura(self, fatura_id, fatura):
        fatura['data_atualizacao'] = datetime.now()
        fatura = self.fatura_repository.atualiza_fatura(fatura_id, fatura)

        return fatura

    def consulta_fatura_todos(self):
        cartoes = self.fatura_repository.consulta_fatura_todos()

        return cartoes

    def consulta_fatura_por_id(self, fatura_id):
        fatura = self.fatura_repository.consulta_fatura_por_id(fatura_id)

        return fatura

    def fatura_generate(self):
        # TODO:
        # captura todas as movimentacoes
        # captura todos os cartoes
        # percorre meses (int)
            # fatura_atual = Fatura()
            # percorre todos os cartoes
                # captura todas as movimentacoes do cartao dentro do periodo definido (dia fechamento)
                # calcula valor 

        pass
