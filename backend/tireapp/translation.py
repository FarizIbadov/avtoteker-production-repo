from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.TireClass)
class TireClassTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(models.OE)
class OETranslationOptions(TranslationOptions):
    fields = ('description',)
