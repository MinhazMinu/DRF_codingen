from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """DRF Create API View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailsAPIView(generics.RetrieveAPIView):
    """DRF Details API View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"
    # lookup_url_kwarg = "product_id"
