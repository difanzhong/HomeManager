from django import template

register = template.Library()


@register.filter(name='add_attr')
def add_css(field, args):
    args = args.strip().split(',')
    if len(args) == 1:
        return field.as_widget(attrs={'class': args[0]})



