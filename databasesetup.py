from django.contrib.auth.models import User
from portal.models import Ingredient, Recipe, RecipeList

# execute with:
# python manage.py shell < databasesetup.py

# create Ingredients
Ingredient(ingredient_name="Hefe", price_per_unit=0.014, unit="g").save()
Ingredient(ingredient_name="Wasser", price_per_unit=0.01, unit="l").save()
Ingredient(ingredient_name="Eier", price_per_unit=0.17, unit="Stück").save()
Ingredient(ingredient_name="Zucker", price_per_unit=0.00065, unit="g").save()
Ingredient(ingredient_name="Salz", price_per_unit=0.014, unit="Prise").save()
Ingredient(ingredient_name="Milch", price_per_unit=0.014, unit="1").save()
butter = Ingredient(ingredient_name="Butter", price_per_unit=0.01, unit="g")
butter.save()
mehl = Ingredient(ingredient_name="Mehl", price_per_unit=0.49, unit="kg")
mehl.save()

# create Recipes
kuchen = Recipe(rezept_bezeichnung="Testrezept")
kuchen.save()
Recipe(rezept_bezeichnung="Sackvoll").save()

# create RecipeIngredients
RecipeList(recipe=kuchen, ingredient=butter, amount=300).save()
RecipeList(recipe=kuchen, ingredient=mehl, amount=300).save()

# create SuperUser
User.objects.create_superuser('admin', 'admin@example.com', 'hallo123')

# create NormalUsers
user_georg = User.objects.create_user('Bäckerei ungebunden', password='hallo123')
user_georg.first_name = "Georg"
user_georg.last_name = "Ungebunden"
user_georg.save()
