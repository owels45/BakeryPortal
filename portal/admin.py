from django.contrib import admin

from portal.models import Order, UserProfile, Ingredient, \
    Recipe, RecipeList, OrderPosition, Invoice

# Register your models here.
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeList)
admin.site.register(OrderPosition)
admin.site.register(Invoice)
