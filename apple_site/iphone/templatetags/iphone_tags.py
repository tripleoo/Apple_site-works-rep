from django import template

# from apple_site.iphone.models import VidTovara

from iphone.models import Iphone, VidTovara, Promo, Review

register = template.Library()

@register.inclusion_tag('vid_tovara.html')
def show_vid():
    vids = VidTovara.objects.all()
    return {"vids": vids}