from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')

    def add_item(self, product, quantity=1):

        # Check if the product is already in the cart
        for item in self.items.all():
            if item.product == product:
                item.quantity += quantity
                item.save()
                return

        # Otherwise, add a new item to the cart
        item = CartItem(product=product, quantity=quantity)
        item.save()
        self.items.add(item)


    def remove_item(self, item_id):
        item = CartItem.objects.get(id=item_id)
        self.items.remove(item)

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

