from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import Product, Category, Basket


class ProductSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'created_date', 'is_active', 'category', 'user', 'user_id', 'category_id'


class CategorySerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'is_active', 'user_id', 'user'


class BasketSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    product = ProductSerializers(read_only=True)
    product_id = ProductSerializers(write_only=True)

    class Meta:
        model = Basket
        fields = 'id', 'user_id', 'product_id'
