from rest_framework import serializers
from .models import * 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Food
        fields = (
            "id",
            "category_name",
            "category",
            "name",
            "description",
            "price",
            "get_image",
            "date_added",
            "comments",
        )

class CategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "foods")

