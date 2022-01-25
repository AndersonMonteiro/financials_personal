from api.serializers.serializers import MetaFinanceiraSerializer
from api.domain.services.meta_financeira_service import MetaFinanceiraService
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class MetaFinanceiraCreateListView(APIView):
    def __init__(self):
        self.meta_financeira_service = MetaFinanceiraService()

    def post(self, request):
        pass

    def get(self, request):
        pass


class MetaFinanceiraUpdateView(APIView):
    def __init__(self):
        self.meta_financeira_service = MetaFinanceiraService()
    
    def patch(self, request, pk):
        pass
