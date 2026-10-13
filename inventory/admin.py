from django.contrib import admin
from .models import ElectronicTool, ElectronicPart

@admin.register(ElectronicTool)
class ElectronicToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'quantity', 'purchase_date')
    search_fields = ('name', 'brand', 'serial_number')

@admin.register(ElectronicPart)
class ElectronicPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'value', 'quantity', 'storage_location')
    search_fields = ('name', 'part_number', 'value')
