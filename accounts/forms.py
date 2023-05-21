from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from allauth.account.forms import SignupForm
from .models import Customer,Address
from django.contrib.auth.models import Group

customUser = get_user_model()

#Customer sign up form. Also used for User sign up
class CustomerSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=11)
    

    def save(self, request):
        user = super(CustomerSignupForm, self).save(request)
        user.is_customer = True
        user.save()
        user_group = Group.objects.get(name='Customer') 
        user.groups.add(user_group)
        
        customer = Customer.objects.create(user=user)
        customer.first_name = self.cleaned_data.get('first_name')
        customer.last_name = self.cleaned_data.get('last_name')
        customer.email = self.cleaned_data.get('email')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()
        
        return user

#Address details form
class AddressForm(forms.Form):
    address1 = forms.CharField(max_length=50)
    address2 = forms.CharField(max_length=50)
    city = forms.CharField(max_length=30)
    post_code = forms.CharField(max_length=10)



#Form which will be used to edit the customer
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number']

#Form which will be used to edit the user
class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


