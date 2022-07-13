from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'image', 'description', 'extra', 'extra_2', 'truncate')