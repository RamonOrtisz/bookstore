from rest_framework import serializers
from product.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]