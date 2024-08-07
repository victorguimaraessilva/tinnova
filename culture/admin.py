from django.contrib import admin

from .models import Culture

class CultureAdmin(admin.ModelAdmin):
    
    fields = [
        'name'
    ]

    list_display = (
        'id', 
        'name',
        'created_at', 
        'updated_at', 
        'deleted_at'
    )

admin.site.register(Culture, CultureAdmin)
