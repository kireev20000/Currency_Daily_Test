from django.contrib import admin

from .models import Сurrency

@admin.register(Сurrency)
class СurrencyAdmin(admin.ModelAdmin):
    list_display = ['date', 'char_code', 'name', 'value',]
    search_fields = ['date', 'char_code', 'name',]
    list_filter = ["char_code", 'date',]
    list_editable = ['value', ]


