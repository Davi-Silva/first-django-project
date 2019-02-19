from django.urls import path
from .views import (
    product_detail_view, 
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    product_update_view
    )


app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product'),
    path('create/', product_create_view, name='create'),
    # path('create/', render_initial_data, name='create')
    path('<int:id>', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]
