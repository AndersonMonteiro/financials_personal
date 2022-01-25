from api.domain.repositories.endereco_repository import EnderecoRepository
from datetime import datetime


class EnderecoService:
    def __init__(self):
        self.endereco_repository = EnderecoRepository()

    def cria_endereco(self, endereco):
        endereco['data_cadastro'] = datetime.now()
        endereco = self.endereco_repository.cria_endereco(endereco)

        return endereco

    def atualiza_endereco(self, endereco_id, endereco):
        endereco['data_atualizacao'] = datetime.now()
        endereco = self.endereco_repository.atualiza_endereco(endereco_id, endereco)
        
        return endereco

    def consulta_endereco_todos(self):
        enderecos = self.endereco_repository.consulta_enderecos_todos()
        
        return enderecos

    def consulta_endereco_por_id(self, endereco_id):
        endereco = self.endereco_repository.consulta_endereco_por_id(endereco_id)

        return endereco
