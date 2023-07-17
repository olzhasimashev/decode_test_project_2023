from rest_framework import generics
from rest_framework import permissions
from products.models import Category
# from articles.permissions import ObjectOwnerOrAdmin
from products.serializers.category import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # filterset_class = DateRangeFilter
    search_fields = ('name', 'id')
    
class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
