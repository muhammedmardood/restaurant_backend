from django.shortcuts import render, HttpResponse
from .serializers import (
        AddOrderedFoodsSerializer, 
        CategorySerializer, 
        FoodSerializer, 
        CommentSerializer, 
        OrderSerializer,
        CustomerSerializer,
        OrderSerializer,
    )
from .models import (
        Category, 
        Food, 
        Comment, 
        OrderItem,
        Customer,
        Order,
    )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_urls(request):
    urls = {
            "Categories: https://mardood.pythonanywhere.com/api/v1.1/categories/",
            "Category Details: https://mardood.pythonanywhere.com/api/v1.1/categorie/[category id]/",
            "Food list: https://mardood.pythonanywhere.com/api/v1.1/food/",
            "Food details: https://mardood.pythonanywhere.com/api/v1.1/food/[food id]/",
            "Comments: https://mardood.pythonanywhere.com/api/v1.1/comments/",
            "Add Comment (using JSON POST request): https://mardood.pythonanywhere.com/api/v1.1/comments/add/",
            "Add a new category (using JSON POST request): https://mardood.pythonanywhere.com/api/v1.1/categories/add/",
            "Add a new food (using JSON POST request): https://mardood.pythonanywhere.com/api/v1.1/food/add",
            "admin page (password and username both are 'admin': https://mardood.pythonanywhere.com/admin/",
        }
    return Response(urls)


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class FoodList(APIView):
    def get(self, request, format=None):
        food = Food.objects.all().order_by("-date_added")
        serializer = FoodSerializer(food, many=True)

        return Response(serializer.data)


class FoodDetail(APIView):
    def get_object(self, pk):
        try:
            return Food.objects.get(id=pk)
        except Food.DoesNotExist:
            HttpResponse("Erorr 404, Not Found")

    def get(self, request, pk, format=None):
        foods = self.get_object(pk)
        serializer = FoodSerializer(foods)
        return Response(serializer.data)

@api_view(["POST"])
def foodAdd(request):
    if request.method == "POST":
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            HttpResponse("Error 404, Not Found")

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def categoryAdd(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

@api_view(["POST"])
def commentsAdd(request):
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

