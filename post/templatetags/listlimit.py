from django import template
register = template.Library()

@register.filter(name="limit")

def limit(data, num):
    return data[:num]