from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, ContactDetails
from .forms import *

class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_customer']

admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Customer)





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



