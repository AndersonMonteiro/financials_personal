from api.models.models import GrupoAcesso
from api.serializers.serializers import GrupoAcessoSerializer
from django.core.exceptions import ObjectDoesNotExist

class GrupoAcessoRepository:
    def cria_grupo_acesso(self, grupo_acesso):
        serializer = GrupoAcessoSerializer(data=grupo_acesso)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_grupo_acesso(self, grupo_acesso_id, grupo_acesso):
        try:
            grupo_acesso_existente = GrupoAcesso.objects.get(pk=grupo_acesso_id)
        except ObjectDoesNotExist:
            return None

        serializer = GrupoAcessoSerializer(
            grupo_acesso_existente, data=grupo_acesso, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_grupo_acesso_todos(self):
        grupo_acesso = GrupoAcesso.objects.all()

        return grupo_acesso
