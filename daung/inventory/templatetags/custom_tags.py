from django import template

from daung.inventory.models import Bin

register = template.Library()

@register.inclusion_tag('includes/menu.html', takes_context=True)
def get_menu(context):
    return {
        'bins': Bin.objects.all(),
        'request': context['request'],
    }

@register.inclusion_tag('includes/nav.html', takes_context=True)
def get_nav(context, header):
    user = context['user']
    return {
        'header': header,
        'user': user,
        'request': context['request'],
    }