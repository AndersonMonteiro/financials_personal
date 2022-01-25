from api.models.models import Endereco
from api.serializers.serializers import EnderecoSerializer
from django.core.exceptions import ObjectDoesNotExist


class EnderecoRepository:

    def cria_endereco(self, endereco):
        serializer = EnderecoSerializer(data=endereco)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_endereco(self, endereco_id, endereco):
        try:
            endereco_existente = Endereco.objects.get(pk=endereco_id)
        except ObjectDoesNotExist:
            return None

        serializer = EnderecoSerializer(
            endereco_existente, data=endereco, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_enderecos_todos(self):
        enderecos = Endereco.objects.all()

        return enderecos

    def consulta_endereco_por_id(self, endereco_id):
        endereco = Endereco.objects.filter(pk=endereco_id).first()

        return endereco

