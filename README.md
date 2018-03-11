For Admin site: /admin/
username: superuser
password: hallo123



Für die Datenbanktabellen Ingredients und Rechnung stehen für die Einheiten und Bezahlstatus nur ein
Integerfeld bereit. Hier ist mal aufgeschlüsselt, wie das aussieht:

Einheiten:
0 - ml
1 - gramm
2 - Stück
3 - 3g (Prise)
4 - noch unbelegt
5 - liter


Rechnungsstatus:
1 - offen
2 - aufgeschoben
3 - bezahlt
-> alle anderen Zahlen führen in der admin-view zu einem "bitte Zahlung überprüfen"