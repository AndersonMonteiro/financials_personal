from api.domain.repositories.comentario_repository import ComentarioRepository
from datetime import datetime


class ComentarioService:
    def __init__(self):
        self.comentario_repository = ComentarioRepository()

    def cria_comentario(self, comentario):
        comentario['data_cadastro'] = datetime.now()
        comentario = self.comentario_repository.cria_comentario(comentario)

        return comentario

    def atualiza_comentario(self, comentario_id, comentario):
        comentario['data_atualizacao'] = datetime.now()
        comentario = self.comentario_repository.atualiza_comentario(comentario_id, comentario)

        return comentario

    def consulta_comentario_todos(self):
        comentarios = self.comentario_repository.consulta_comentario_todos()

        return comentarios

    def consulta_comentario_por_id(self, comentario_id):
        comentario = self.comentario_repository.consulta_comentario_por_id(comentario_id)

        return comentario
