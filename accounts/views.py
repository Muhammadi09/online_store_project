from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.views import SignupView
from .forms import CustomerSignupForm, CustomerForm, UserForm, AddressForm
from .models import Customer, Address



class CustomerSignupView(SignupView):

    template_name = 'registration/signup.html'
    form_class = CustomerSignupForm
    view_name = 'customer_signup'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
customer_signup = CustomerSignupView.as_view()


def ProfileView(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer_form = CustomerForm(instance=customer)
    user_form = UserForm(instance = request.user)
    
    template = 'account/profile.html'
    context = {'user_form': user_form, 'customer_form':customer_form, 'customer':customer}
    return render(request, template, context)

def ProfileEditView(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer_form = CustomerForm(instance=customer)
    user_form = UserForm(instance = request.user)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        user_form = UserForm(request.POST, instance=request.user)

        if customer_form.is_valid() and user_form.is_valid():
            customer_form.save()
            user_form.save()
            return redirect('profile',request.user.id)

    template = 'account/profile_edit.html'
    context = {'user_form': user_form, 'customer_form':customer_form, 'customer':customer}
    
    return render(request, template, context)


def AddAddressView(request, pk):
    # Retrieve the relevant customer object
    customer = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        address_form = AddressForm(request.POST)

        #Check if form entry is valid.
        if address_form.is_valid():
            # Create a new Address object with the form data
            address = Address(
                address1 = address_form.cleaned_data['address1'],
                address2 = address_form.cleaned_data['address2'],
                city = address_form.cleaned_data['city'],
                post_code = address_form.cleaned_data['post_code']
            )
            
            # Save the Address object to the database
            address.save()

            # Add the Address object to the customer's addresses
            customer.addresses.add(address)

            # Save the customer object to the database
            customer.save()

            # Redirect to the customer's profile page
            return redirect('profile', request.user.id)
        
    else:  
        # Create a blank form instance
        address_form = AddressForm()

    
    return render(request, 'account/add_address.html', {'address_form': address_form})


def updateAddressView(request, customer_pk, address_id):
    # Retrieve the relevant customer and address objects
    customer = get_object_or_404(Customer, pk=customer_pk)
    address = get_object_or_404(Address, id=address_id)

    if request.method == 'POST':
        #check if value of input submit button is 'update'
        if request.POST.get('confirmation') == 'update':
            # Create a form instance and populate it with data from the request
            form = AddressForm(request.POST)

            if form.is_valid():
                # Update the Address object with the form data
                address.address1 = form.cleaned_data['address1']
                address.address2 = form.cleaned_data['address2']
                address.city = form.cleaned_data['city']
                address.post_code = form.cleaned_data['post_code']

                # Save the Address object to the database
                address.save()

                # Redirect to the customer's detail page
                return redirect('profile', pk=customer_pk)
        else:
            return redirect('confirm_delete_address', customer.pk, address.id)
            
    else:
        # Populate the form with the existing address data
        form = AddressForm(initial={
            'address1': address.address1,
            'address2': address.address2,
            'city': address.city,
            'post_code': address.post_code,
        })

    return render(request, 'account/update_address.html', {'form': form, 'customer': customer, 'address': address})

def confirm_delete_address(request, customer_pk, address_id):
    #get current customer and address object
    customer = get_object_or_404(Customer, pk=customer_pk)
    address = get_object_or_404(Address, id=address_id)

    if request.method == 'POST':
        # If the user submitted the confirmation form, check the form field value
        if request.POST.get('confirmation') == 'confirm':
            # If the user confirmed the deletion, delete the address object and redirect to the customer's detail page
            address.delete()
            #return to customer profile page
            return redirect('profile', customer.pk)
        else:
            #cancel the deletion and go back to update_address  page
            return redirect('update_address', customer.pk, address.id)
        
# If the user accessed the confirmation page, display the confirmation template
    return render(request, 'account/confirm_delete_address.html', {'customer': customer, 'address': address})