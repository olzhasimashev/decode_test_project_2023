from rest_framework import serializers
from products.models import Category
# from user.serializers import BaseUserInfoSerializer


class CategorySerializer(serializers.ModelSerializer):
    # owner = BaseUserInfoSerializer(read_only=True)

    # def to_representation(self, instance):
    #     self.fields['name'] = CategorySerializer(many=True, read_only=True, context={"request": self.context['request']})
    #     return super(CategorySerializer, self).to_representation(instance)

    class Meta:
        model = Category
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['name'] = self.context['request'].user
    #     validated_data['article_id'] = self.context['view'].kwargs['id']
    #     return super().create(validated_data)
