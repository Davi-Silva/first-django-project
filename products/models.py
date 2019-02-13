from django.db import models

# Create your models here.
class Product(models.Model):
    # max_length = required
    title       = models.CharField(max_length=120) 
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000, default=0.00)
    # blank=True means that this field is required to submuit the form to the DB / null=True means that the following column in the DB can be empty.
    summary     = models.TextField(blank=True, null=True) 
    feature     = models.BooleanField() #null=True, default=True


