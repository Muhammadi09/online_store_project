from django.db import models


class Category(models.Model):

    CATEGORY_CHOICES = (
        ('books', 'Books'), 
        ('home', 'Home'),
        ('clothes', 'Clothes'),
        ('health', 'Health'),
        ('electronic', 'Electronic'),
        ('misc', 'Misc'),
    )
    category_name = models.CharField(
        max_length=25,
        choices=CATEGORY_CHOICES,
        default='misc'
    )

    def __str__(self):
        return self.category_name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=6)

    def __str__(self):
        return self.title









