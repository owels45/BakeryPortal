from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name="order"),
    path('myorders/', views.myorders, name='myorders'),
    path('myinvoices/', views.myinvoices, name='myinvoices')
]