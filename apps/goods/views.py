

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer
class GoodsListView(APIView):
    """
    List all goods.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_data = GoodsSerializer(goods, many=True)
        return Response(goods_data.data)