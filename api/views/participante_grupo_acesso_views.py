from api.serializers.serializers import ParticipanteGrupoAcessoSerializer
from api.domain.services.participante_grupo_acesso_service import ParticipanteGrupoAcessoService
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


class ParticipanteGrupoAcessoCreateList(APIView):
    def __init__(self):
        self.participante_grupo_acesso_service = ParticipanteGrupoAcessoService()

    def get(self, request):
        queryset = self.participante_grupo_acesso_service.consulta_participante_grupo_acesso_todos()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = ParticipanteGrupoAcessoSerializer(page, many=True)

        if page is not None:
            return paginator.get_paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParticipanteGrupoAcessoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        participante_grupo_acesso = self.participante_grupo_acesso_service.cria_participante_grupo_acesso(request.data)

        return Response(grupo_acesso, status=status.HTTP_201_CREATED)

class ParticipanteGrupoAcessoUpdate(APIView):
    
    def __init__(self):
        self.participante_grupo_acesso_service = ParticipanteGrupoAcessoService()

    def path(self, request, pk):
        serializer = ParticipanteGrupoAcessoSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        participante_grupo_acesso_serialized = self.participante_grupo_acesso_service.atualiza_participante_grupo_acesso(
            pk, serializer.data)

        return Response(participante_grupo_acesso_serialized, status=status.HTTP_201_CREATED)
