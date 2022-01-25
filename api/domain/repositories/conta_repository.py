from api.models.models import Conta
from api.serializers.serializers import ContaSerializer
from django.core.exceptions import ObjectDoesNotExist


class ContaRepository:
    def consulta_contas(self):
        contas = Conta.objects.all()

        return contas

    def consulta_conta_por_id(self, conta_id):
        conta = Conta.objects.filter(pk=conta_id).first()

        return conta

    def cria_conta(self, conta):
        serializer = ContaSerializer(data=conta)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_conta(self, conta_id, conta):
        try:
            conta_existente = Conta.objects.get(pk=conta_id)
        except ObjectDoesNotExist:
            return None

        serializer = ContaSerializer(
            conta_existente, data=conta, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

