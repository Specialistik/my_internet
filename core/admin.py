import uuid
from django.contrib import admin
from django.contrib.auth.models import *
from .models import Person, Operator, Role


class PersonAdmin(admin.ModelAdmin):
    fields = ('login', 'password', 'role', 'fio', 'passport', 'address', 'sim', 'operator_type', 'passport_pic', 'passport_pic2', 'token')
    list_display = ('login', 'password', 'fio', 'passport', 'sim', 'address', 'operator_type', 'passport_pic', 'passport_pic2')
    search_fields = ('login', 'password', 'fio', 'passport', 'token', 'sim', 'address', 'operator_type')

    def save_model(self, request, obj, form, change):
        if not obj.token:
            obj.token = str(uuid.uuid4())
        super().save_model(request, obj, form, change)


admin.site.register(Person, PersonAdmin)
admin.site.register(Operator)
admin.site.register(Role)
#admin.site.unregister(User)
#admin.site.unregister(Group)
