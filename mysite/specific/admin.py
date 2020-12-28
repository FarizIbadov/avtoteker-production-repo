from django.contrib import admin
from .models import Country, Season, Brand, Serie

admin.site.site_header = "Avto Teker Admin"

admin.site.register(Country)
admin.site.register(Season)
admin.site.register(Brand)
admin.site.register(Serie)
