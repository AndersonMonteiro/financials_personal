from api.models.models import ParticipanteGrupoAcesso
from api.serializers.serializers import ParticipanteGrupoAcessoSerializer
from django.core.exceptions import ObjectDoesNotExist

class ParticipanteGrupoAcessoRepository:
    def cria_participante_grupo_acesso(self, participante_grupo_acesso):
        serializer = ParticipanteGrupoAcessoSerializer(data=participante_grupo_acesso)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_participante_grupo_acesso(self, participante_grupo_acesso_id, participante_grupo_acesso):
        try:
            participante_grupo_acesso_existente = ParticipanteGrupoAcesso.objects.get(pk=participante_grupo_acesso_id)
        except ObjectDoesNotExist:
            return None

        serializer = ParticipanteGrupoAcessoSerializer(
            participante_grupo_acesso_existente, data=participante_grupo_acesso, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_participante_grupo_acesso_todos(self):
        participantes = ParticipanteGrupoAcesso.objects.all()

        return participantes
