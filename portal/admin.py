from django.contrib import admin
from portal.models import Bestellung, BestellPositionen, Rechnung, User, Zutaten, Zutatenliste, Rezept
# Register your models here.


admin.site.register(Bestellung)
admin.site.register(BestellPositionen)
admin.site.register(Rechnung)
admin.site.register(User)
admin.site.register(Zutaten)
admin.site.register(Zutatenliste)
admin.site.register(Rezept)