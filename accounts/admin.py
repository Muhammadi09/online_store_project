from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, ContactDetails
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = UserRegForm
    form = UserRegChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff',]


class ContactDetailsInLine(admin.TabularInline):
    model = ContactDetails.customer.through

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailsInLine,
    ]
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(Customer)
admin.site.register(ContactDetails)


