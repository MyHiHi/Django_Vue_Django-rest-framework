

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer,GoodsModelSerializer
# 传输JSON数据


class GoodsListView1(APIView):
    """
    List all goods.
    """
    # 方法一
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_data = GoodsSerializer(goods, many=True)
    #     return Response(goods_data.data)
    #方法二
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_data = GoodsModelSerializer(goods, many=True)
        return Response(goods_data.data)
    
#方法三
from rest_framework import mixins,generics
from rest_framework.pagination import PageNumberPagination

class GoodsListPagination(PageNumberPagination):
    # 一个页面的条数
    page_size = 5
    page_size_query_param = 'page_size'
    #http://127.0.0.1/goods2/?p=2 修改p的 如果page_query_param='poo' 那么http://127.0.0.1/goods2/?poo=2
    page_query_param='p'
    max_page_size = 100

class GoodsListView2(generics.ListAPIView):
    # 商品列表页
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerializer
    pagination_class=GoodsListPagination


from rest_framework import viewsets

class GoodsListView3(mixins.ListModelMixin,viewsets.GenericViewSet):
    # queryset= Goods.objects.all()
    serializer_class=GoodsModelSerializer
    pagination_class=GoodsListPagination
    def get_queryset(self):
        price_min=int (self.request.query_params.get('price_min',0))
        return Goods.objects.filter(shop_price__gte=price_min)
        
        



    
