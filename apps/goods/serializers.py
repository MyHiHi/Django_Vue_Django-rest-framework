from datetime import datetime
from rest_framework import serializers
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    goods_num = serializers.IntegerField(default=0)
    goods_front_image=serializers.ImageField()
    add_time = serializers.DateTimeField(default=datetime.now)
