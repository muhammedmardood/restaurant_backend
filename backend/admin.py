from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Comment)

