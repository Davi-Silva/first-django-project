from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view, render_initial_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('product/', product_detail_view, name='product'),
    # path('create/', product_create_view, name='create'),
    path('create/', render_initial_data, name='create')
]
