from rest_framework import serializers

from product.models import Product
from order.models import Order
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Product
        fields = ['product', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')
        order = Order.objects.create(validated_data)
        for product in product_data:
            order.product.add(product)
        return order