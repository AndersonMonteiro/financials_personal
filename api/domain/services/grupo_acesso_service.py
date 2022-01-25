from api.domain.repositories.grupo_acesso_repository import GrupoAcessoRepository
from datetime import datetime


class GrupoAcessoService:
    def __init__(self):
        self.grupo_acesso_repository = GrupoAcessoRepository()

    def cria_grupo_acesso(self, grupo_acesso):
        grupo_acesso['data_cadastro'] = datetime.now()
        grupo_acesso = self.grupo_acesso_repository.cria_grupo_acesso(grupo_acesso)

        return grupo_acesso

    def atualiza_grupo_acesso(self, grupo_acesso_id, grupo_acesso):
        grupo_acesso['data_atualizacao'] = datetime.now()
        grupo_acesso = self.grupo_acesso_repository.atualiza_grupo_acesso(grupo_acesso_id, grupo_acesso)

        return grupo_acesso

    def consulta_grupo_acesso_todos(self):
        grupos_acesso = self.grupo_acesso_repository.consulta_grupo_acesso_todos()

        return grupos_acesso
