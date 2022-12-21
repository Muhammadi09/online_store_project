from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import SignupForm
from .models import *

customUser = get_user_model()

class CustomerSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    GENDER_CHOICES = (('male', 'male'), ('female', 'female'),)
    gender = forms.ChoiceField(choices = GENDER_CHOICES)

    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    post_code = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=11)

    def save(self, request):
        user = super(CustomerSignupForm, self).save(request)
        customer_user = Customer(
            user = user,
            first_name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            email = self.cleaned_data.get('email'),
            gender = self.cleaned_data.get('gender'),
        )
        contact_details_user = ContactDetails(
            address1 = self.cleaned_data.get('address1'),
            address2 = self.cleaned_data.get('address2'),
            city = self.cleaned_data.get('city'),
            post_code = self.cleaned_data.get('post_code'),
            phone_number = self.cleaned_data.get('phone_number'),
        ) 
        customer_user.save()
        contact_details_user.save()
        contact_details_user.customer.add(customer_user)
        return customer_user.user

class UserRegForm(UserCreationForm):
    
    class Meta:
        model = customUser
        fields = ('email', 'first_name', 'last_name')

class UserRegChangeForm(UserChangeForm):
    
    class Meta:
        model = customUser
        fields = ('email', 'first_name', 'last_name')


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