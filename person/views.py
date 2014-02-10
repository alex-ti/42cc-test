# -*- coding: utf8 -*-
from annoying.decorators import render_to

from person.models import Person

@render_to('detail/contact_info.html')
def personView(request):
    person = Person.objects.all()[0]
    return {'person': person}
