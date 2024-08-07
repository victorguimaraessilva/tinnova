from django.contrib import admin
from .models import Producer


class ProducerAdmin(admin.ModelAdmin):
    fields = [
        'document',
        'producer_name',
        'farm_name',
        'city',
        'state',
        'total_area',
        'arable_area',
        'vegetation_area',
        'cultures'
    ]

    list_display = (
        'id', 
        'producer_name', 
        'document', 
        'farm_name', 
        'city', 
        'state', 
        'created_at', 
        'updated_at', 
        'deleted_at'
    )

admin.site.register(Producer, ProducerAdmin)
