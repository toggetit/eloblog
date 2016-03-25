from django.contrib import admin

from .models import Entry

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Entry, SummernoteModelAdmin)
