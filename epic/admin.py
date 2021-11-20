"""# Register your models here.
from django.contrib import admin
from django.contrib import admin
from django.contrib import admin

from .models import *

admin.site.register(Product)"""
from django.contrib import admin


from .models import *
admin.site.register(Product)
from .category import Category
admin.site.register(Category)
from .customer import Customer
admin.site.register(Customer)

