from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.Add)
class AddTranslationOptions(TranslationOptions):
    fields = ('image',)