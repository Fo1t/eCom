from django import template
import markdown

register = template.Library()

@register.filter(name='toFixed')
def toFixed(value):
    return '%.1f' % value

@register.filter(name='toInt')
def toInt(value):
    return int(value)

@register.filter(name='cutStr')
def cutStr(value):
    return value[:15]

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()