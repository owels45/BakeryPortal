from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name="order"),
    path('myorders/', views.myorders, name='myorders'),
    path('myinvoices/', views.myinvoices, name='myinvoices'),
    path('myinvoice/', views.invoicedetail, name='invoicedetail'),
    path('recipes/', views.RecipesView.as_view(), name='recipe_list'),
    path('register/complete/', views.registration_complete, name='registration_complete'),
    path('recipes/add_recipe', views.add_recipe, name='add_recipe'),
    path('recipes/recipe_ingredients', views.add_ingredient, name='recipe_ingredients'),
    path('recipes/recipe_list', views.RecipesView.as_view(), name='recipe_list')
]