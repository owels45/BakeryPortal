"""BakeryPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from portal import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('portal/', include('portal.urls')),
                  path('', RedirectView.as_view(url='/portal/')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('register/', views.register, name='registration'),
                  path('register/complete/', views.registration_complete, name='registration_complete'),
                  path('recipes/add_recipe', views.add_recipe, name='add_recipe'),
                  path('recipes/recipe_ingredients', views.add_ingredient, name='recipe_ingredients'),
                  #path('recipes/add_recipe_complete', views.add_recipe_complete, name='add_recipe_complete'),
                  path('recipes/recipe_list', views.RecipesView.as_view(), name='recipe_list')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
