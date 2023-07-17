from rest_framework import serializers
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

class ProductsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description', 'photo', 'price', 'category')