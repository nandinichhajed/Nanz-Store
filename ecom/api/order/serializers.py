from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user',)
        # fields = ('user', 'product_name', 'total_product')
        # TODO: add product and quantity
        