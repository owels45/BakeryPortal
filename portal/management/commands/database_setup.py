from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from portal.models import UserProfile, Ingredient, Recipe, RecipeList

# run with python manage database_setup

class Command(BaseCommand):
    help = "Initializes basic database entries."

    def handle(self, *args, **options):
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
        kuchen = Recipe(rezept_bezeichnung="Kuchen")
        kuchen.save()
        mehlsack = Recipe(rezept_bezeichnung="Sackvoll Mehl")
        mehlsack.save()

        # create RecipeIngredients
        RecipeList(recipe=kuchen, ingredient=butter, amount=300).save()
        RecipeList(recipe=kuchen, ingredient=mehl, amount=0.5).save()
        RecipeList(recipe=mehlsack, ingredient=mehl, amount=100).save()

        # create SuperUser
        User.objects.create_superuser('superuser', 'admin@example.com', 'hallo123')

        # create NormalUsers
        user_georg = User.objects.create_user('Bäckerei ungebunden', password='hallo123')
        user_georg.first_name = "Georg"
        user_georg.last_name = "Ungebunden"
        user_georg.save()

        # create Bakery-Profile
        UserProfile(user=user_georg, bakery_name="Bäckerei ungebunden", adress_street="Musterstraße",
                    adress_street_number=10, adress_plz="0815", adress_city="Mosbach").save()

        print("Inserted sample entries into the database.")
