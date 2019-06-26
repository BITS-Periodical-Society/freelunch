from django import template

register = template.Library()

@register.filter
def cap(value):
    namelist = value.split(' ')
    fixed = ''
    for name in namelist:
        name = name.lower()
        # fixes mcdunnough
        if name.startswith('mc'):
            sub = name.split('mc')
            name = "Mc" + sub[1].capitalize()
        # fixes "o'neill"
        elif name.startswith('o\''): 
            sub = name.split('o\'')
            name = "O'" + sub[1].capitalize()

        else: name = name.capitalize()
        
        nlist = name.split('-')
        for n in nlist:
            if len(n) > 1:
                up = n[0].upper()
                old = "-%s" % (n[0],)
                new = "-%s" % (up,)
                name = name.replace(old,new)

        fixed = fixed + " " + name
    return fixed