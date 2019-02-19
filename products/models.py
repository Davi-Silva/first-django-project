from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    # max_length = required
    title       = models.CharField(max_length=120) 
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000, default=0.00)
    # blank=True means that this field is required to submuit the form to the 
    # DB / null=True means that the following column in the DB can be empty.
    email       = models.EmailField(default="-", blank=False, null=False)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id" : self.id}) # f"./{self.id}/"

class Course(models.Model):
    title       = models.CharField(max_length=30)
    description = models.TextField(default='')
    price       = models.DecimalField(max_digits=1000, decimal_places=2)
