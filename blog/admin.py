from django.contrib import admin

# Register your models here.
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
        list_display = ('title', 'edate', 'cdate')

admin.site.register(Entry, EntryAdmin)
