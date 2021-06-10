from django import template
from sticker.models import Sticker,StickerTimer

register = template.Library()

@register.simple_tag(name="get_stickers")
def get_stickers(obj):
    sticker_id_list = filter(None, obj.stickers.split(","))
    stickers = Sticker.objects.filter(id__in=map(int,sticker_id_list))
    return stickers

@register.simple_tag(name="get_sticker_timer")
def get_sticker_timer():
    sticker_timer = StickerTimer.objects.filter(active=True).first()
    if sticker_timer:
        return sticker_timer.interval
    return 2000
