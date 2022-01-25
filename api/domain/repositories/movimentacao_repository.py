from api.models.models import Movimentacao
from api.serializers.serializers import MovimentacaoSerializer
from django.core.exceptions import ObjectDoesNotExist
from simple_history.utils import bulk_create_with_history


class MovimentacaoRepository:

    def cria_movimentacao(self, movimentacao):
        serializer = MovimentacaoSerializer(data=movimentacao)

        if serializer.is_valid():
            serializer.save()

        return serializer.data
    
    def cria_movimentacao_bulk(self, movimentacoes):
        batch_size = 1000

        bulk_create_with_history(movimentacoes, Movimentacao, batch_size=batch_size)

        return None

    def atualiza_movimentacao(self, movimentacao_id, movimentacao):
        try:
            movimentacao_existente = Movimentacao.objects.get(
                pk=movimentacao_id)
        except ObjectDoesNotExist:
            return None

        serializer = MovimentacaoSerializer(
            movimentacao_existente, data=movimentacao, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_movimentacao_todos(self):
        movimentacoes = Movimentacao.objects.all()

        return movimentacoes

    def consulta_movimentacao_por_id(self, movimentacao_id):
        movimentacao = Movimentacao.objects.filter(pk=movimentacao_id).first()

        return movimentacao
