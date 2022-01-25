from api.domain.repositories.meta_financeira_repository import MetaFinanceiraRepository
from datetime import datetime

class MetaFinanceiraService:
    def __init__(self):
        self.meta_financeira_repository = MetaFinanceiraRepository()

    def cria_meta_financeira(self, meta_financeira):
        pass

    def atualiza_meta_financeira(self, id, meta_financeira):
        pass

    def consulta_metas_financeiras(self):
        pass

    def consulta_metas_financeiras_por_id(self, id):
        pass
