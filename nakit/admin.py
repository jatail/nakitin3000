from django.contrib import admin
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin
# Register your models here.

class NakkiAdmin(admin.ModelAdmin):
    list_display = ('task', 'event_name', 'event_org', 'date', 'starttime', 'endtime', 'personcount')
    list_filter = ('date',)
    list_select_related = True
    def event_name(self, instance):
        return instance.event.name
    def event_org(self, instance):
        return instance.event.organizer.name

class OrgAdminAdmin(admin.ModelAdmin):
    list_display= ('organization', 'person', 'first_name', 'last_name')
    list_filter = ('organization', 'person')
    def organization(self, instance):
        return instance.organization.name
    def first_name(self, instance):
        return instance.person.first_name
    def last_name(self, instance):
        return instance.person.last_name

class NakittautuminenAdmin(admin.ModelAdmin):
    list_display = ('taski', 'taskdate', 'first_name', 'last_name')
    def taski(self, instance):
        return instance.nakki.task
    def taskdate(self, instance):
        return instance.nakki.date
    def first_name(self, instance):
        return instance.person.first_name
    def last_name(self, instance):
        return instance.person.last_name

class EventAdmin(admin.ModelAdmin):
    list_display= ('name', 'date', 'venue', 'organizer', 'createdby')
    list_filter = ('organizer', 'createdby', 'date')

admin.site.register(Organization)
admin.site.register(Event, EventAdmin)
admin.site.register(Nakki, NakkiAdmin)
admin.site.register(Nakittautuminen, NakittautuminenAdmin)
admin.site.register(Orgadmin, OrgAdminAdmin)