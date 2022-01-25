from api.domain.repositories.participante_grupo_acesso_repository import ParticipanteGrupoAcessoRepository
from datetime import datetime

class ParticipanteGrupoAcessoService:
    def __init__(self):
        self.participante_grupo_acesso_repository = ParticipanteGrupoAcessoRepository()

    def cria_participante_grupo_acesso(self, participante_grupo_acesso):
        participante_grupo_acesso['data_cadastro'] = datetime.now()
        participante_grupo_acesso = self.participante_grupo_acesso_repository.cria_participante_grupo_acesso(participante_grupo_acesso)

        return participante_grupo_acesso

    def atualiza_participante_grupo_acesso(self, participante_grupo_acesso_id, participante_grupo_acesso):
        participante_grupo_acesso['data_atualizacao'] = datetime.now()
        participante_grupo_acesso = self.participante_grupo_acesso_repository.atualiza_participante_grupo_acesso(participante_grupo_acesso_id, participante_grupo_acesso)

        return participante_grupo_acesso

    def consulta_participante_grupo_acesso_todos(self):
        participantes_grupo_acesso = self.participante_grupo_acesso_repository.consulta_participante_grupo_acesso_todos()

        return participantes_grupo_acesso
