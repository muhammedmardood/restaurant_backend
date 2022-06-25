from django.urls import path
from .views import *

urlpatterns = [
    path("", api_urls),
    path("categories/", CategoryList.as_view()),
    path("categories/<int:pk>/", CategoryDetail.as_view()),
    path("food/", FoodList.as_view()),
    path("food/<int:pk>/", FoodDetail.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/add/", commentsAdd),
    path("categories/add/", categoryAdd),
    path("food/add/", foodAdd),
]
