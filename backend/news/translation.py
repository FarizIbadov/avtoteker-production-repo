from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'image', 'description', 'extra', 'truncate')