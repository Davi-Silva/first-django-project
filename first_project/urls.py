from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
]
