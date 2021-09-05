from django.contrib import admin
from .models import Make,Model,Year,Trim,TireSize

def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)
make_inactive.short_description = "Deactivete"

def make_active(modeladmin, request, queryset):
    queryset.update(active=True)
make_active.short_description = "Activete"

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ['name','active']
    readonly_fields = ['slug']

    fields = (('name','active'),'slug')
    list_filter = ['active']

    actions = [make_inactive,make_active]

    def get_queryset(self,request):
        return self.model.objects.all().order_by('name')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name','make','active']
    list_filter = ['active','make']
    readonly_fields = ['slug','make']

    fields = (('name','active'),'slug','make')

    actions = [make_inactive,make_active]

    def get_queryset(self,request):
        return self.model.objects.all().order_by('make')

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['name','model','make','active']
    readonly_fields = ['model','make','slug']
    list_filter = ['active','model']

    fields = (('name','active'),'model','make','slug') 

    actions = [make_inactive,make_active]

@admin.register(Trim)
class TrimAdmin(admin.ModelAdmin):
    list_display = ['name','model','make','year','active']
    readonly_fields = ['model','make','slug','year']
    list_filter = ['active','model','make','year']
    fields = (('name','active'),'model','make','year','slug') 

    actions = [make_inactive,make_active]



@admin.register(TireSize)
class TireSizeAdmin(admin.ModelAdmin):
    list_display = ['trim','tire_type','tire','rim','pressure']
    list_filter = ['trim']

    fields = ('trim','tire_type','tire','rim')
    readonly_fields = ('trim','tire_type','tire','rim','pressure')