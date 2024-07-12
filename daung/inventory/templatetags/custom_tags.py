from django import template

from daung.inventory.models import Bin

register = template.Library()

@register.inclusion_tag('includes/menu.html', takes_context=True)
def get_bins(context):
    return {
        'bins': Bin.objects.all(),
        'request': context['request'],
    }