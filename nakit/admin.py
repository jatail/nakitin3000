from django.contrib import admin
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin, Eventmaker
# Register your models here.

admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Nakki)
admin.site.register(Nakittautuminen)
admin.site.register(Orgadmin)
admin.site.register(Eventmaker)