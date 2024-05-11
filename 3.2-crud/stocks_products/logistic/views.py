from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'address']

    pagination_class = LimitOffsetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    ordering_fields = ['id', 'address']
    # при необходимости добавьте параметры фильтрации

    def get_queryset(self):
        queryset = Stock.objects.all()
        product_name = self.request.query_params.get("search")
        if product_name:
            queryset = queryset.filter(products__title__icontains=product_name)
        return queryset

    pagination_class = LimitOffsetPagination
