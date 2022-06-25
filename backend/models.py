from django.db import models
from django.db.models.expressions import OrderBy
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(
        Category, related_name="foods", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images", null=False, blank=False)
    date_added = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return "https://mardood.pythonanywhere.com" + self.image.url
        else:
            return "The Image Couldn't Be Found"


class Comment(models.Model):
    food = models.ForeignKey(
        Food, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(editable=False, auto_now_add=True)
    stars = models.IntegerField(default=0)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.comment

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    food = models.ForeignKey(
        Food,
        related_name='food',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    order = models.ForeignKey(
            Order,
            related_name='order_items',
            on_delete=models.SET_NULL,
            blank=True,
            null=True
            )
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.food.price * self.quantity

    @property
    def get_food_name(self):
        return self.food.name

    def __str__(self):
        return self.food.name

    class Meta:
        ordering = ('-date_added',)
