from django import template
from campaign.models import Post

register = template.Library()

@register.simple_tag(name="get_campaigns")
def get_campains(obj):
    campaigns_id_list = filter(None, obj.campaigns.split(","))
    campaigns = Post.objects.filter(id__in=map(int,campaigns_id_list),active=True)
    return campaigns
