from datetime import datetime
from rest_framework import serializers
from .models import Goods,GoodsCategory
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    goods_num = serializers.IntegerField(default=0)
    goods_front_image=serializers.ImageField()
    add_time = serializers.DateTimeField(default=datetime.now)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Goods.objects.create(**validated_data)
class CategoryModelSerializer2(serializers.ModelSerializer):
    """
    商品第二类类别序列化
    """
    class Meta:
        model=GoodsCategory
        fields='__all__'

class CategoryModelSerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat=CategoryModelSerializer2(many=True)
    class Meta:
        model=GoodsCategory
        fields='__all__'


class GoodsModelSerializer(serializers.ModelSerializer):
    category=CategoryModelSerializer()
    class Meta:
        model=Goods
        # 引入Goods所有字段
        fields='__all__'
        # fields=('name','click_num','shop_price','goods_brief','goods_front_image','add_time')

