from django.urls import path, include
from .views import FoodApiView, CommentApiView, CartApiView, CartItemApiView
# urlpatterns = [
# 	path('food-list/', FoodApiView.as_view(), name='food-list')

# ]

from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('food-list', FoodApiView, basename='food-list')
router.register('comment-list', CommentApiView, basename='comment-list')
router.register('cart', CartApiView, basename='cart')
router.register('cart-item', CartItemApiView, basename='cartitem')
urlpatterns = [
    path('', include(router.urls)),
]
