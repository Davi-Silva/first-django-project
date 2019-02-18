from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=10)
    my_context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", my_context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    my_context = {
        'form': form
    }
    return render(request, "products/product_create.html", my_context)

