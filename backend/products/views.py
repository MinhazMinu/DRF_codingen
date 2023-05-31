from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDetailsAPIView(generics.RetrieveAPIView):
    """DRF API View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"
    # lookup_url_kwarg = "product_id"
