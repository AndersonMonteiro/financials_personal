from api.domain.repositories.perfil_repository import PerfilRepository
from datetime import datetime


class PerfilService:
    def __init__(self):
        self.perfil_repository = PerfilRepository()

    def cria_perfil(self, perfil):
        perfil['data_cadastro'] = datetime.now()
        perfil = self.perfil_repository.cria_perfil(perfil)

        return perfil

    def atualiza_perfil(self, perfil_id, perfil):
        perfil['data_atualizacao'] = datetime.now()
        perfil = self.perfil_repository.atualiza_perfil(perfil_id, perfil)

        return perfil

    def consulta_perfil_todos(self):
        perfis = self.perfil_repository.consulta_perfil_todos()
        
        return perfis

    def consulta_perfil_por_id(self, perfil_id):
        perfil = self.perfil_repository.consulta_perfil_por_id(perfil_id)

        return perfil
