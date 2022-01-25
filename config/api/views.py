from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import FoodSerializer, CommentSerializer, CartSerializer, CartItemSerializer
from foods.models import Foods, Comment
from carts.models import Cart, CartItems
from .permissions import IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
# from django.views.decorators.http import require_POST

# ----------------------------------------------------------
class FoodApiView(ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
# ----------------------------------------------------------
class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly,]
# ----------------------------------------------------------
class CartApiView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthorOrReadOnly,]
# ----------------------------------------------------------
# ----------------------------------------------------------
class CartItemApiView(ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthorOrReadOnly,]
# ----------------------------------------------------------