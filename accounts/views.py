from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from .forms import CustomerSignupForm, CustomerForm, UserForm
from django.contrib.auth import get_user_model
from .models import Customer




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


        

    

    