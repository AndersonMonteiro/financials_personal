from api.domain.repositories.conta_repository import ContaRepository
from datetime import datetime


class ContaService:
    def __init__(self):
        self.conta_repository = ContaRepository()

    def consulta_contas(self):
        contas = self.conta_repository.consulta_contas()

        return contas

    def consulta_conta_por_id(self, conta_id):
        conta = self.conta_repository.consulta_conta_por_id(conta_id)

        return conta

    def cria_conta(self, conta):
        conta['data_cadastro'] = datetime.now()
        conta = self.conta_repository.cria_conta(conta)

        return conta

    def atualiza_conta(self, conta_id, conta):
        conta['data_atualizacao'] = datetime.now()
        conta = self.conta_repository.atualiza_conta(conta_id, conta)

        return conta
