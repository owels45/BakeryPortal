from django.db import models

# Alle Feldtypen in Django: https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    prename = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    bakeryName = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    plz = models.CharField(max_length=5)

    def __str__(self):
        return self.prename + " " + self.name + " " + self.bakeryName


class Zutaten(models.Model):
    zutatenBez = models.CharField(max_length=100)
    einheit = models.PositiveIntegerField()  # Per Vereinbarung händeln wir die Einheiten der Zutaten extra
    pricePerUnit = models.FloatField()

    def __str__(self):
        return self.zutatenBez


class Rezept(models.Model):
    rezeptBez = models.CharField(max_length=200)

    def __str__(self):
        return self.rezeptBez


class Zutatenliste(models.Model):
    rezept = models.ForeignKey(Rezept, on_delete=False)
    zutat = models.ForeignKey(Zutaten, on_delete=False)


class Bestellung(models.Model):
    user = models.ForeignKey(User, on_delete=False)
    bestellDatum = models.DateTimeField('date published')

    def __str__(self):
        return str(self.id)


class BestellPositionen(models.Model):
    bestellung = models.ForeignKey(Bestellung, on_delete=False)
    rezept = models.ForeignKey(Rezept, on_delete=False)
    menge = models.PositiveIntegerField()
    alsTeig = models.BooleanField()


class Rechnung(models.Model):
    #rechnung = models.AutoField(primary_key=True)
    bestellung = models.ForeignKey(Bestellung, on_delete=False)
    rechnungsDatum = models.DateField()
    bezahlStatus = models.PositiveIntegerField()

