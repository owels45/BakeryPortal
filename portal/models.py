from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Alle Feldtypen in Django: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bakeryName = models.CharField(max_length=200)
    adress_street = models.CharField(max_length=200)
    adress_street_number = models.PositiveIntegerField()
    adress_street_number_extra = models.CharField(max_length=2, blank=True)
    adress_plz = models.CharField(max_length=5)
    adress_city = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.bakeryName


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)
    pricePerUnit = models.FloatField()

    # Per Vereinbarung händeln wir die Einheiten der Zutaten extra
    UNIT = (
        ('ml', 'Milliliter'),
        ('l', 'Liter'),
        ('g', 'Gramm'),
        ('mg', 'Milligramm'),
        ('Stück', 'Stück'),
        ('Prise/n', 'Prise/n (3g)'),
    )
    unit = models.CharField(max_length=6, choices=UNIT, blank=True, help_text='Einheit')

    def __str__(self):
        return f'{self.ingredientName} {self.unit}'


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
        return self.recipe.rezeptBez + " - " + self.ingredient.ingredientName + " " + str(self.amount) + " " + self.ingredient.unit


class Order(models.Model):
    kunde = models.ForeignKey(User, on_delete=False)
    bestellDatum = models.DateTimeField('date published')
    rezepte = models.ManyToManyField(Recipe, through='OrderPosition')

    def __str__(self):
        return str(self.id) + ': ' + str(self.kunde) + ' ' + str(self.bestellDatum)


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

    BEZAHL_STATUS = (
        ('offen', 'offen'),
        ('aufgeschoben', 'aufgeschoben'),
        ('bezahlt', 'bezahlt'),
        ('unbekannt', 'bitte Rechnung prüfen'),
    )
    bezahlStatus = models.CharField(max_length=12, choices=BEZAHL_STATUS, blank=False, default='bitte Rechnung prüfen', help_text='Status des Bezahlvorgangs')

    def __str__(self):
        return str(self.order.id) + ": " + str(self.rechnungsDatum) + " " + self.bezahlStatus
