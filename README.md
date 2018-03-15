# For Admin site: /admin/
username: superuser
password: hallo123

# User ohne Berechtigungen
username: firstUser
password: firstpassword


# Getting Server Startet:
Innerhalb von PyCharm im Terminal auf das Verzeichnis `.\BakeryPortal\` wechseln. (Das muss das
Verzeichnis sein, in der auch die `manage.py` liegt). Dort dann den Befehl `python manage.py runserver` eingeben.
Der Server sollte jetzt laufen und ist unter `localhost:8000/admin` oder `127.0.0.1:8000/admin` erreichbar. Als
Anmeldedaten die oben genannten verwenden.


# Datenbankfeatures ausprobieren:
* Alle Datenbankinformationen lassen sich unter `localhost:8000` einsehen.
* Ohne den Server zu starten, können auch alle Funktionen, die Python auf der Datenbank ausführen kann, könne auch über das Terminal abgesendet werden.
    1. Shell öffnen: `python manage.py shell`
    2. Datenbanktabellen holen: `from portal.models import Customer, Ingredient, Recipe, RecipeList, Order, OrderPosition, Invoice`
    3. Neue Datenbankobjekte erzeugen: `i = Ingredient(ingredientName="Käse", einheit=1, pricePerUnit = 0.02)`
    4. Jedes erzeugte Objekt muss __immer__ gespeichert werden: `ì.save()`
    5. Das gerade angelegte Objekt angucken: `i`
    6. Alle Objekte in Ingredients anschauen: `Ingredient.objects.all()`
    7. Nur eine gewisse Auswahl anzeigen lassen: `Ingredient.objects.filter(ingredientName="Käse")`


Für die Datenbanktabellen Ingredients und Rechnung stehen für die Einheiten und Bezahlstatus nur ein
Integerfeld bereit. Hier ist mal aufgeschlüsselt, wie das aussieht:

**Einheiten:**
0 - ml  
1 - gramm
2 - Stück  
3 - 3g (Prise)  
4 - noch unbelegt  
5 - liter  


**Rechnungsstatus:**  
1 - offen  
2 - aufgeschoben  
3 - bezahlt  
-> alle anderen Zahlen führen in der admin-view zu einem "bitte Zahlung überprüfen"  
