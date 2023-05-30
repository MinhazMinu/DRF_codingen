from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    print(type(model_data.title))
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title"])
    return JsonResponse(data)
