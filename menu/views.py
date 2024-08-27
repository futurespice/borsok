from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import DishSearchForm
from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_description="Добавление нового блюда",
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_FORM, description="Название блюда", type=openapi.TYPE_STRING),
            openapi.Parameter('description', openapi.IN_FORM, description="Описание блюда", type=openapi.TYPE_STRING),
            openapi.Parameter('price', openapi.IN_FORM, description="Цена блюда", type=openapi.TYPE_STRING),
            openapi.Parameter('image', openapi.IN_FORM, description="Изображение блюда", type=openapi.TYPE_FILE),
            openapi.Parameter('is_special_offer', openapi.IN_FORM, description="Специальное предложение", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('category', openapi.IN_FORM, description="ID категории блюда", type=openapi.TYPE_INTEGER),
        ],
        responses={201: DishSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DishesByCategoryView(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=slug)
        return Dish.objects.filter(category=category)


class DishSearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Название блюда", type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, description="Slug категории", type=openapi.TYPE_STRING)
        ],
        responses={200: DishSerializer(many=True)}
    )
    def get(self, request):
        """
        Поиск блюд по названию и категории
        """
        form = DishSearchForm(request.GET or None)
        queryset = Dish.objects.all()

        if form.is_valid():
            name = form.cleaned_data.get('name')
            category = form.cleaned_data.get('category')

            if name:
                queryset = queryset.filter(name__icontains=name)
            if category:
                queryset = queryset.filter(category=category)

        serializer = DishSerializer(queryset, many=True)
        return Response(serializer.data)


class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer