from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display =  ('title', 'date_event', 'date_create')
    list_filter = ('title','user',)


admin.site.register(Evento, EventoAdmin)