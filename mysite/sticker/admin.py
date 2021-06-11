from django.contrib import admin
from . import models,forms

# Register your models here.
@admin.register(models.Sticker)
class StickerAdmin(admin.ModelAdmin):
    readonly_fields = ("image_width_num",'text_width_num')
    list_display = ('text','image','active')
    form = forms.StickerForm

    fields = (
        'color',
        'image',
        ('text','text_font'),
        ('image_width','image_width_num'),
        ('text_width','text_width_num'),
        'description',
        'active'
    )

    def image_width_num(self,obj):
        return f"{round(obj.image_width,2)}%"

    def text_width_num(self,obj):
        return f"{round(obj.text_width,2)}%"

