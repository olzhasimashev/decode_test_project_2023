from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
# from articles.filter import DateRangeFilter
from products.models import Products
from products.serializers.products import ProductsSerializer, ProductsCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductsList(generics.ListAPIView):
    queryset = Products.objects.filter(is_available=True)
    serializer_class = ProductsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # filterset_class = DateRangeFilter
    search_fields = ('name', 'id')
    
class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
class ProductsCreate(generics.CreateAPIView):
    serializer_class = ProductsCreateSerializer


# class ArticleDetail(generics.RetrieveAPIView):
#     lookup_field = 'id'
#     queryset = Article.objects.filter(moderated=True).order_by('-created_at', 'views')
#     serializer_class = ArticleDetailSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.increase_views()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
