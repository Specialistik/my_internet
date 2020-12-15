from django.contrib import admin
from django.contrib.auth.models import *
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'fio', 'passport', 'sim',)
    search_fields = ('login', 'password', 'fio', 'passport', 'sim',)


admin.site.register(Person, PersonAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
