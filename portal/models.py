from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Alle Feldtypen in Django: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bakery_name = models.CharField(max_length=200)
    adress_street = models.CharField(max_length=200)
    adress_street_number = models.PositiveIntegerField()
    adress_street_number_extra = models.CharField(max_length=2, blank=True)
    adress_plz = models.CharField(max_length=5)
    adress_city = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.bakery_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    price_per_unit = models.FloatField()

    # Per Vereinbarung händeln wir die Einheiten der Zutaten extra
    UNIT = (
        ('ml', 'Milliliter'),
        ('l', 'Liter'),
        ('g', 'Gramm'),
        ('kg', 'Kilogramm'),
        ('Stück', 'Stück'),
        ('Tropfen', 'Tropfen'),
        ('Prise/n', 'Prise/n (3g)'),
    )
    unit = models.CharField(max_length=12, choices=UNIT, blank=True, help_text='Einheit')

    def __str__(self):
        return f'{self.ingredient_name} in {self.unit}'


class Recipe(models.Model):
    rezept_bezeichnung = models.CharField(max_length=200)

    def __str__(self):
        return self.rezept_bezeichnung


class RecipeList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=False)
    amount = models.FloatField()

    def __str__(self):
        return self.recipe.rezept_bezeichnung + " - " + self.ingredient.ingredient_name + " " + str(self.amount) + " " + self.ingredient.unit


class Order(models.Model):
    kunde = models.ForeignKey(User, on_delete=False)
    bestell_datum = models.DateTimeField('date published')

    def __str__(self):
        return str(self.id) + ': ' + str(self.id) + ' ' + str(self.bestell_datum)


class OrderPosition(models.Model):
    bestellung = models.ForeignKey(Order, on_delete=True)
    rezept = models.ForeignKey(Recipe, on_delete=True)
    menge = models.PositiveIntegerField()
    als_teig = models.BooleanField()

    def __str__(self):
        return "Bestellnummer: " + str(self.bestellung.id) + " - Rezept: " + self.rezept.rezept_bezeichnung + " - Menge: " + str(self.menge)


class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=False)
    rechnungs_datum = models.DateField()
    rechnungs_summe = models.FloatField()

    BEZAHL_STATUS = (
        ('offen', 'offen'),
        ('aufgeschoben', 'aufgeschoben'),
        ('bezahlt', 'bezahlt'),
        ('unbekannt', 'bitte Rechnung prüfen'),
    )
    bezahl_status = models.CharField(max_length=12, choices=BEZAHL_STATUS, blank=False, default='bitte Rechnung prüfen', help_text='Status des Bezahlvorgangs')

    def __str__(self):
        return str(self.order.id) + ": " + str(self.rechnungs_datum) + " " + self.bezahl_status
