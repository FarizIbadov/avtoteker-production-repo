from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(models.Serie)
class SerieTranslationOptions(TranslationOptions):
    fields = ('description', 'extra')