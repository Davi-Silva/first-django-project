from django.contrib import admin
from django.urls import include, path
from pages.views import (
    home_view, 
    contact_view, 
    about_view, 
    social_view,
    )


urlpatterns = [
    path('product/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
]
