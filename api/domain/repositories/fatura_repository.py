from api.models.models import Fatura
from api.serializers.serializers import FaturaSerializer
from django.core.exceptions import ObjectDoesNotExist


class FaturaRepository:
    def cria_fatura(self, fatura):
        serializer = FaturaSerializer(data=fatura)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_fatura(self, fatura_id, fatura):
        try:
            fatura_existente = Fatura.objects.get(pk=fatura_id)
        except ObjectDoesNotExist:
            return None

        serializer = FaturaSerializer(
            fatura_existente, data=fatura, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_fatura_todos(self):
        cartoes = Fatura.objects.all()

        return cartoes

    def consulta_fatura_por_id(self, fatura_id):
        fatura = Fatura.objects.filter(pk=fatura_id).first()

        return fatura

