from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('content',)
