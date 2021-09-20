from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.Copyright)
class CopyrightTranslationOptions(TranslationOptions):
    fields = ('content',)