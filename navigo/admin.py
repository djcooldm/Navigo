from django.contrib import admin
from .models import Vehicle, Listing

class VehicleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Vehicle._meta.fields]
    
admin.site.register(Vehicle)
admin.site.register(Listing)
