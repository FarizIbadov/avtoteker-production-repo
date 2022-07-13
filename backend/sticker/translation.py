from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.Sticker)
class StickerTranslationOptions(TranslationOptions):
    fields = ('text', 'description')