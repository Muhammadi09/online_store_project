from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer,Address, CustomerAddress
from .forms import *

class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_customer']


class AddressInline(admin.TabularInline):
    model = CustomerAddress
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address')




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address)
admin.site.register(CustomerAddress, CustomerAddressAdmin)
admin.site.register(get_user_model(), CustomUserAdmin)







# class ContactDetailsInLine(admin.TabularInline):
#     model = ContactDetails.customer.through

# class CustomerAdmin(UserAdmin):
#     model = Customer
#     add_form = UserRegForm
#     form = UserRegChangeForm
#     # inlines = [
#     #     ContactDetailsInLine,
#     # ]
#     list_display = ('first_name', 'last_name', 'email',)

# admin.site.register(ContactDetails)



