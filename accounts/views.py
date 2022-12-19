from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from accounts.forms import CustomerRegForm, UserRegForm, ContactDetailsRegForm

def SignUpCustomer(request):

    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        customer_form = CustomerRegForm(request.POST)
        customer_contact_details_form = ContactDetailsRegForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid() and customer_contact_details_form.is_valid:
            user = user_form.save()
            customer = customer_form.save(commit=False)
            contact_details = customer_contact_details_form.save(commit=False)
            customer.user = user
            customer.first_name = user.first_name
            customer.last_name = user.last_name
            customer.email = user.email
            customer.save()
            contact_details.save()
            customer.contact_details.add(contact_details)
           
            
            return redirect('login')
    else:
        user_form = UserRegForm()
        customer_form = CustomerRegForm()
        customer_contact_details_form = ContactDetailsRegForm()
    return render(
        request,
        'registration/signup.html',
        {'user_form': user_form, 'customer_form': customer_form, 'customer_contact_details_form': customer_contact_details_form}
    )

    # form_class = CustomerRegForm
    # success_url = reverse_lazy('login')
    # template_name = 'registration/signup.html'