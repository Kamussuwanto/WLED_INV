from django.db import models

class ElectronicTool(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=100, unique=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    
    # Target physical LED index on the WS2812B chain for this tool drawer
    led_index = models.PositiveIntegerField(default=0, help_text="WS2812B LED number for this drawer slot")

    def __str__(self):
        return f"{self.name} ({self.brand})"

class ElectronicPart(models.Model):
    name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100, unique=True, blank=True)
    value = models.CharField(max_length=50, blank=True) # e.g., "10k ohm", "100uF"
    package_type = models.CharField(max_length=50, blank=True) # e.g., "SMD", "Through-hole"
    quantity = models.PositiveIntegerField(default=0)
    storage_location = models.CharField(max_length=100, blank=True) # e.g., "Bin A3"
    
    # Target physical LED index on the WS2812B chain for this component bin
    led_index = models.PositiveIntegerField(default=0, help_text="WS2812B LED number for this bin slot")

    def __str__(self):
        return f"{self.name} - {self.value}"
