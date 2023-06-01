# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
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


class ProductUpdateAPIView(generics.UpdateAPIView):
    """DRF Details API View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # instance.save()

        # title = serializer.validated_data.get("title")
        # content = serializer.validated_data.get("content") or None
        # if content is None:
        #     content = title
        # serializer.save(content=content)


class ProductDeleteAPIView(generics.DestroyAPIView):
    """DRF Details API View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)

#         queryset = Product.objects.all(raise_exception=True)
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content") or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors)
