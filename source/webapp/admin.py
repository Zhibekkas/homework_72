from django.contrib import admin
from webapp.models import Citation


class CitationAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'name', 'rating', 'status', 'added_date']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['text', 'name', 'rating', 'status', 'added_date']
    readonly_fields = ['added_date']

admin.site.register(Citation, CitationAdmin)
