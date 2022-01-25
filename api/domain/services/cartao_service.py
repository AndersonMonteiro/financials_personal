from api.domain.repositories.cartao_repository import CartaoRepository
from datetime import datetime


class CartaoService:
    def __init__(self):
        self.cartao_repository = CartaoRepository()

    def cria_cartao(self, cartao):
        cartao['data_cadastro'] = datetime.now()
        cartao = self.cartao_repository.cria_cartao(cartao)

        return cartao

    def atualiza_cartao(self, cartao_id, cartao):
        cartao['data_atualizacao'] = datetime.now()
        cartao = self.cartao_repository.atualiza_cartao(cartao_id, cartao)

        return cartao

    def consulta_cartao_todos(self):
        cartoes = self.cartao_repository.consulta_cartao_todos()

        return cartoes

    def consulta_cartao_por_id(self, cartao_id):
        cartao = self.cartao_repository.consulta_cartao_por_id(cartao_id)

        return cartao
