from api.models.models import Cartao
from api.serializers.serializers import CartaoSerializer
from django.core.exceptions import ObjectDoesNotExist


class CartaoRepository:
    def cria_cartao(self, cartao):
        serializer = CartaoSerializer(data=cartao)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_cartao(self, cartao_id, cartao):
        try:
            cartao_existente = Cartao.objects.get(pk=cartao_id)
        except ObjectDoesNotExist:
            return None

        serializer = CartaoSerializer(
            cartao_existente, data=cartao, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_cartao_todos(self):
        cartoes = Cartao.objects.all()

        return cartoes

    def consulta_cartao_por_id(self, cartao_id):
        cartao = Cartao.objects.filter(pk=cartao_id).first()

        return cartao
