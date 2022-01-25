from rest_framework import serializers
from foods.models import Foods, Comment
from carts.models import Cart, CartItems
class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Foods
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = CartItems
		fields = '__all__'