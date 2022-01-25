from api.domain.repositories.orcamento_repository import OrcamentoRepository
from datetime import datetime

class OrcamentoService:
    def __init__(self):
        self.orcamento_repository = OrcamentoRepository()

    def cria_orcamento(self, orcamento):
        pass

    def atualiza_orcamento(self, id, orcamento):
        pass

    def consulta_orcamentos(self):
        pass

    def consulta_orcamentos_por_id(self, id):
        pass
