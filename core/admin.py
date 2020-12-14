from django.contrib import admin

from .models import Person, Role

admin.site.register(Role)
admin.site.register(Person)
