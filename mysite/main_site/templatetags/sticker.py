from django import template
from sticker.models import StickerTimer

register = template.Library()

@register.simple_tag(name="get_sticker_timer")
def get_sticker_timer():
    sticker_timer = StickerTimer.objects.filter(active=True).first()
    if sticker_timer:
        return sticker_timer.interval
    return 2000
