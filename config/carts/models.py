from django.db import models
from contact.models import Contact
from foods.models import Foods
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order = models.BooleanField(default=False)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class CartItems(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Foods, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	quantity = models.IntegerField(default=1)
	def __str__(self):
		return str(self.total_price)


	def __str__(self):
		return str(self.product.food_name)
@receiver(post_save, sender=Cart)
def correct_price(sender, **kwargs):
	cart_items = kwargs['instance']
	price_of_product = Foods.objects.get(id=cart_items.product.id)
	cart_items.price = cart_items.quantity * float(price_of_product.price)
	total_cart_items = CartItems.objects.filter(user=cart_items.user)
	# cart_items.total_items = len(total_cart_items)
	cart = Cart.objects.get(id=cart_items.cart.id)
	cart.total_price = cart_items.price
	cart.save()
