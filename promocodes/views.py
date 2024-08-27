from rest_framework import generics
from .models import PromoCode
from .serializers import PromoCodeSerializer


class PromoCodeListView(generics.ListAPIView):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
