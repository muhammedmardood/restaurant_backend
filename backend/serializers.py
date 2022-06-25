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

class AddOrderedFoodsSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source="food.name")
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "quantity",
            "date_added",
            "food",
            "food_name",
            "order",
            "get_total",
        )

class OrderSerializer(serializers.ModelSerializer):
    order_items = AddOrderedFoodsSerializer(many=True)
    customer_name = serializers.CharField(source="customer.name")
    
    class Meta:
        model = Order
        fields = (
            "customer",
            "customer_name", 
            "date_ordered",
            "completed",
            "address",
            "order_id",
            "order_items",
        )

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "__all__"
        )
