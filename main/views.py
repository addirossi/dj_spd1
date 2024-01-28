from django.http import HttpResponse, Http404
from django.shortcuts import render

from main.models import Product


def index_page(request):
    return HttpResponse("Hello world!")


def products_list(request):
    products = Product.objects.all()
    template = "list.html"
    return render(request, template, {"products": products})


def product_details(request, product_id):
    try:
        print(f"ИДЕНТИФИКАТОР: {product_id}")
        product = Product.objects.get(id=product_id)
        template = "details.html"
        return render(request, template, {"product": product})
    except Product.DoesNotExist:
        raise Http404