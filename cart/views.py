from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from menu.models import Dish
from .serializers import CartSerializer, CartItemSerializer
from django.utils import timezone
from promocodes.models import PromoCode

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        # Убедитесь, что сессия существует. Если нет — создайте её.
        if not self.request.session.session_key:
            self.request.session.create()

        session_key = self.request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
        return cart


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        session_key = self.request.session.session_key or self.request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=session_key)

        # Проверяем, что блюдо существует в базе данных
        dish_id = request.data.get('dish_id')
        dish = get_object_or_404(Dish, id=dish_id)

        quantity = int(request.data.get('quantity', 1))

        # Ищем товар в корзине или создаем новый, если его еще нет
        cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)

        # Обновляем количество товара
        cart_item.quantity = quantity
        cart_item.save()

        return Response({'message': 'Блюдо добавлено/обновлено в корзине'}, status=status.HTTP_200_OK)


class DecreaseCartItemView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer  # Добавьте это

    def update(self, request, *args, **kwargs):
        session_key = self.request.session.session_key
        cart = Cart.objects.get(session_key=session_key)
        cart_item = CartItem.objects.get(id=kwargs['id'], cart=cart)

        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
            return Response({'message': 'Товар удален из корзины'}, status=status.HTTP_200_OK)
        cart_item.save()

        return Response({'message': 'Количество товара уменьшено', 'quantity': cart_item.quantity},
                        status=status.HTTP_200_OK)


class IncreaseCartItemView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer  # Добавьте это

    def update(self, request, *args, **kwargs):
        session_key = self.request.session.session_key
        cart = Cart.objects.get(session_key=session_key)
        cart_item = CartItem.objects.get(id=kwargs['id'], cart=cart)

        cart_item.quantity += 1
        cart_item.save()

        return Response({'message': 'Количество товара увеличено', 'quantity': cart_item.quantity},
                        status=status.HTTP_200_OK)


class RemoveFromCartView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_field = 'id'

    def get_queryset(self):
        session_key = self.request.session.session_key
        cart = Cart.objects.get(session_key=session_key)
        return CartItem.objects.filter(cart=cart)



class ApplyPromoCodeView(generics.UpdateAPIView):
    serializer_class = CartSerializer  # Используем сериализатор корзины

    def update(self, request, *args, **kwargs):
        session_key = self.request.session.session_key
        cart = Cart.objects.get(session_key=session_key)

        promo_code = request.data.get('promo_code')
        if promo_code:
            try:
                promo = PromoCode.objects.get(code=promo_code, is_active=True)
                if promo.expiration_date >= timezone.now():
                    cart.promo_code = promo
                    cart.save()
                    return Response({'message': 'Промокод успешно применен'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Промокод истек'}, status=status.HTTP_400_BAD_REQUEST)
            except PromoCode.DoesNotExist:
                return Response({'error': 'Неверный промокод'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Необходимо указать промокод'}, status=status.HTTP_400_BAD_REQUEST)


