from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *

customUser = get_user_model()

class UserRegForm(UserCreationForm):
    
    class Meta:
        model = customUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomerRegForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('gender',)
    
class CustomerRegChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('gender',)
    

class ContactDetailsRegForm(forms.ModelForm):
    
    class Meta:
        model = ContactDetails
        fields = ('address1', 'address2', 'city', 'post_code', 'phone_number',)