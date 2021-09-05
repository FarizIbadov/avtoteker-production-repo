from django.contrib import admin
from .models import Phone,SocialMedia,Address

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class SocialMediaAdmin(admin.ModelAdmin):
    pass