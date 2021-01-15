import uuid
import string
import random

from django.contrib import admin
from django.contrib.auth.models import *
from .models import Person, Operator, Emails, Company, Region, Payment

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)

class PersonAdmin(admin.ModelAdmin):
    fields = ( 'fio', 'passport', 'address', 'sim', 'operator_type', 'passport_pic', 'passport_pic2', 'company', 'balans', 'monthly_payment', 'payment_date')
    list_display = ('login', 'password', 'fio', 'passport', 'sim', 'address', 'operator_type', 'passport_pic', 'passport_pic2', 'company', 'balans', 'monthly_payment', 'payment_date')
    search_fields =  ('login', 'password', 'fio', 'passport', 'sim', 'address', 'operator_type', 'company', 'balans', 'monthly_payment', 'payment_date')

    def save_model(self, request, obj, form, change):
        if not obj.token:
            obj.token = str(uuid.uuid4())
            obj.login = 'user' + str(obj.id) 
            obj.password = get_random_alphanumeric_string(8)
        super().save_model(request, obj, form, change)


admin.site.register(Person, PersonAdmin)
admin.site.register(Operator)
admin.site.register(Emails)
admin.site.register(Company)
admin.site.register(Region)
admin.site.register(Payment)

admin.site.unregister(User)
admin.site.unregister(Group)
