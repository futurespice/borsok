from rest_framework import generics, status
from rest_framework.response import Response
from cart.models import Cart
from .models import Order
from .serializers import OrderSerializer


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        session_key = self.request.session.session_key
        cart = Cart.objects.filter(session_key=session_key).first()

        if not cart:
            return Response({'error': 'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)

        if not request.data.get('address'):
            return Response({'error': 'Адрес обязателен для оформления заказа'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(
            cart=cart,
            address=request.data['address']
        )
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

