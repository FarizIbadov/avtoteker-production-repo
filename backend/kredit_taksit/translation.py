from modeltranslation.translator import TranslationOptions, register
from . import models

@register(models.KreditTaksitImage)
class KreditTaksitImageTranslationOptions(TranslationOptions):
    fields = ("description",)