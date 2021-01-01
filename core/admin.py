import uuid
from django.contrib import admin
from django.contrib.auth.models import *
from .models import Person, Operator, Emails, Company, Region

class PersonAdmin(admin.ModelAdmin):
    fields = ('login', 'password', 'fio', 'passport', 'address', 'sim', 'operator_type', 'passport_pic', 'passport_pic2', 'token', 'company')
    list_display = ('login', 'password', 'fio', 'passport', 'sim', 'address', 'operator_type', 'passport_pic', 'passport_pic2', 'company')
    search_fields = ('login', 'password', 'fio', 'passport', 'token', 'sim', 'address', 'operator_type', 'company')

    def save_model(self, request, obj, form, change):
        if not obj.token:
            obj.token = str(uuid.uuid4())
        super().save_model(request, obj, form, change)


admin.site.register(Person, PersonAdmin)
admin.site.register(Operator)
admin.site.register(Emails)
admin.site.register(Company)
admin.site.register(Region)
admin.site.unregister(User)
admin.site.unregister(Group)
