from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=10)
    my_context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", my_context)

# Create a form view
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('../')

    my_context = {
        'form': form
    }
    return render(request, "products/product_create.html", my_context)

# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     my_context = {}
#     return render(request, "products/product_create.html", my_context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # new the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     my_context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", my_context)

# Render initial data in the form from DB
def render_initial_data(request):
    initial_data = {
        "title": "This is my awesome title"
    }
    obj = Product.objects.get(id=20)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form" : form
    }
    return render(request, "products/product_create.html", context)

# Dynamic link to product urls
def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)

# Delete product from the DB
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        "object" : obj
    }
    return render(request, "products/product_delete.html", context)

# List of the products from the DB
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("../../")
    context = {
        "form" : form
    }
    return render(request, "products/product_create.html", context)

