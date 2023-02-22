from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_children(context, item):
    return context['menu_items'].filter(parent=item).prefetch_related('children').active(context['request']).menu(context['menu_name'])
