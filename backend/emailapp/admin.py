from django.contrib import admin
from . import models

@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    pass

@admin.register(models.AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    pass
