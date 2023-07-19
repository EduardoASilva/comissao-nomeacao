from django import template

register = template.Library()


@register.filter
def abbreviate_name(value):
    n = len(value)
    name = value.split(" ")

    for na in name:
        m = na.lower()
        if len(na) <= 3 or m == "de" or m == "da" or m == "dos":
            name.remove(na)

    name_completed = name[0] + " " + name[1] + " " + name[-1]
    return name_completed
