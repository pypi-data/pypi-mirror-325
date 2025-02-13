from django import template

register = template.Library()

@register.filter
def timedelta_days(first, second):
    return (first - second).days
