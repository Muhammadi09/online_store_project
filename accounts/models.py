from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_customer = models.BooleanField('customer status',default=False)
    

class Customer(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, primary_key=True, related_name='customer_profile')
    phone_number = models.CharField(max_length=11, default='')
    addresses = models.ManyToManyField('Address', through='CustomerAddress')

    def __str__(self):
        return "ID: {0} | Name: {1} {2} | Email: {3} ".format(self.user.pk, self.user.first_name, self.user.last_name, self.user.email)


class Address(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=20)
    customers = models.ManyToManyField('Customer', through='CustomerAddress')

    def __str__(self):
        return "{0}, {1}, {2}".format(self.address1, self.city, self.post_code)
    

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)





# class Employee(models.Model):
#     user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='employee_profile')
#     DEPARTMENT_CHOICES = (
#         ('administrator', 'administrator'),
#         ('sales', 'sales'),
#         ('customer_service', 'customer_service'),
#     )
#     department = models.Choices = DEPARTMENT_CHOICES

#     def __str__(self):
#         return "{0} - {1}".format(self.user.email, self.department)

