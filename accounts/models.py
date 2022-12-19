from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass


class Customer(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='customer_profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    GENDER_CHOICES = (('male', 'male'), ('female', 'female'),)

    gender = models.CharField(
        max_length=7,
        choices=GENDER_CHOICES,
        default='male'
    )
    
    def __str__(self):
        return "{0} {1} | {2} | {3}".format(self.first_name, self.last_name, self.email, self.gender)


class ContactDetails(models.Model):
    customer = models.ManyToManyField(
        Customer,
        related_name='contact_details'
    )
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.address1, self.city, self.post_code)


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

