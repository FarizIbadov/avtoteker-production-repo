from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.TireListMessage)
class TireListMessageTranslationOptions(TranslationOptions):
    fields = ('text',)