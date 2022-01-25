from api.models.models import Comentario
from api.serializers.serializers import ComentarioSerializer
from django.core.exceptions import ObjectDoesNotExist


class ComentarioRepository:
    def cria_comentario(self, comentario):
        serializer = ComentarioSerializer(data=comentario)

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def atualiza_comentario(self, comentario_id, comentario):
        try:
            comentario_existente = Comentario.objects.get(pk=comentario_id)
        except ObjectDoesNotExist:
            return None

        serializer = ComentarioSerializer(
            comentario_existente, data=comentario, partial=True
        )

        if serializer.is_valid():
            serializer.save()

        return serializer.data

    def consulta_comentario_todos(self):
        comentarios = Comentario.objects.all()

        return comentarios

    def consulta_comentario_por_id(self, comentario_id):
        comentario = Comentario.objects.filter(pk=comentario_id).first()

        return comentario
