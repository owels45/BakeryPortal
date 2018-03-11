from django.db import models


# Alle Feldtypen in Django: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types

class Customer(models.Model):
    kunden_id = models.AutoField(primary_key=True)
    prename = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    bakeryName = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    plz = models.CharField(max_length=5)

    def __str__(self):
        return self.prename + " " + self.name + " - " + self.bakeryName


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)
    einheit = models.PositiveIntegerField()  # Per Vereinbarung händeln wir die Einheiten der Zutaten extra
    pricePerUnit = models.FloatField()

    def __str__(self):
        if self.einheit == 0:
            unit = "ml"
        elif self.einheit == 1:
            unit = "gramm"
        elif self.einheit == 2:
            unit = "stück"
        elif self.einheit == 3:
            unit = "Prise (3g)"
        elif self.einheit == 4:
            unit = ""
        elif self.einheit == 5:
            unit = "liter"
        else:
            unit = ""
        return self.ingredientName + " (in " + unit + ")"


class Recipe(models.Model):
    rezeptBez = models.CharField(max_length=200)
    zutat = models.ManyToManyField(Ingredient, through='RecipeList')

    def __str__(self):
        return self.rezeptBez


class RecipeList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=False)
    amount = models.FloatField()

    def __str__(self):
        if self.ingredient.einheit == 0:
            unit = "ml"
        elif self.ingredient.einheit == 1:
            unit = "gramm"
        elif self.ingredient.einheit == 2:
            unit = "stück"
        elif self.ingredient.einheit == 3:
            unit = "Prise (3g)"
        elif self.ingredient.einheit == 4:
            unit = ""
        elif self.ingredient.einheit == 5:
            unit = "liter"
        else:
            unit = ""
        return self.recipe.rezeptBez + " - " + self.ingredient.ingredientName + " " + str(self.amount) + " " + unit


class Order(models.Model):
    kunde = models.ForeignKey(Customer, on_delete=False)
    bestellDatum = models.DateTimeField('date published')
    rezepte = models.ManyToManyField(Recipe, through='OrderPosition')

    def __str__(self):
        return str(self.id)


class OrderPosition(models.Model):
    bestellung = models.ForeignKey(Order, on_delete=True)
    rezept = models.ForeignKey(Recipe, on_delete=True)
    menge = models.IntegerField()
    asTeig = models.BooleanField()

    def __str__(self):
        return "Bestellnummer: "+ str(self.bestellung.id) + " - Rezept: " + self.rezept.rezeptBez + " - Menge: " + str(self.menge)


class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=False)
    rechnungsDatum = models.DateField()
    bezahlStatus = models.PositiveIntegerField()

    def __str__(self):
        if self.bezahlStatus == 0:
            bezahlstatus = "offen"
        elif self.bezahlStatus == 1:
            bezahlstatus = "aufgeschoben"
        elif self.bezahlStatus == 2:
            bezahlstatus = "bezahlt"
        else:
            bezahlstatus = "bitte Rechnung überprüfen"
        return str(self.order.id) + " " + str(self.rechnungsDatum) + " " + str(bezahlstatus)
