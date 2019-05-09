

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,GoodsModelSerializer,CategoryModelSerializer
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

# 实现shop_price过滤
# 方法一
class GoodsListView3(mixins.ListModelMixin,viewsets.GenericViewSet):
    # queryset= Goods.objects.all()
    serializer_class=GoodsModelSerializer
    pagination_class=GoodsListPagination
    def get_queryset(self):
        price_min=int (self.request.query_params.get('price_min',0))
        return Goods.objects.filter(shop_price__gte=price_min)
        
        

# 方法二

    
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters
class GoodsListView4(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页、分页、搜索、过滤、排序
    """
    queryset= Goods.objects.all()
    serializer_class=GoodsModelSerializer
    pagination_class=GoodsListPagination
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    # filterset_fields = ('name', 'shop_price')
    filterset_class=GoodsFilter
    search_fields =('name','goods_desc')
    ordering_fields = ('sold_num','add_time')


class CategoryViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    获取商品分类列表
    """
    queryset=GoodsCategory.objects.filter(category_type=1)
    serializer_class=CategoryModelSerializer

