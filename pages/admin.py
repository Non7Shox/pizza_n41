from django.contrib import admin

from pages.models import ScrollModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('created_at',)
