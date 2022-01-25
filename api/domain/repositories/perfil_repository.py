from api.models.models import Perfil
from api.serializers.serializers import PerfilSerializer
from django.core.exceptions import ObjectDoesNotExist


class PerfilRepository:

    def cria_perfil(self, perfil):
        serializer = PerfilSerializer(data=perfil)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_perfil(self, perfil_id, perfil):
        try:
            perfil_existente = Perfil.objects.get(pk=perfil_id)
        except ObjectDoesNotExist:
            return None

        serializer = PerfilSerializer(
            perfil_existente, data=perfil, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_perfil_todos(self):
        perfis = Perfil.objects.all()

        return perfis

    def consulta_perfil_por_id(self, perfil_id):
        perfil = Perfil.objects.filter(pk=perfil_id).first()

        return perfil

