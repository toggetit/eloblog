from django.contrib import admin

from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'isDraft', 'cdate', 'edate')

admin.site.register(Entry, EntryAdmin)
