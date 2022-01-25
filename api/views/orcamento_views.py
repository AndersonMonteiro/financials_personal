from api.serializers.serializers import OrcamentoSerializer
from api.domain.services.orcamento_service import OrcamentoService
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class OrcamentoCreateListView(APIView):
    def __init__(self):
        self.orcamento_service_service = OrcamentoService()

    def post(self, request):
        pass

    def get(self, request):
        pass


class OrcamentoUpdateView(APIView):
    def __init__(self):
        self.orcamento_service_service = OrcamentoService()
    
    def patch(self, request, pk):
        pass
