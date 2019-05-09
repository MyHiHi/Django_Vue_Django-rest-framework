from django_filters import rest_framework as filter 
from .models import Goods
class GoodsFilter(filter.FilterSet):
    price_max=filter.NumberFilter(field_name='shop_price',lookup_expr='gte');
    price_min=filter.NumberFilter(field_name='shop_price',lookup_expr='lte');
    name=filter.CharFilter(field_name='name',lookup_expr='icontains');

    class Meta:
        model=Goods
        fields=['price_max','price_min','name']
