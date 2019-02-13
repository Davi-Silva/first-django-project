from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.TextField(default='New course')
    description = models.TextField(default='This is a description of the new course...')
    price = models.TextField(default='99.99')
    

class OldCourses(models.Model):
    title = models.TextField(default='Old course')
    description = models.TextField(default='This is a description of the old course...')
    price = models.TextField(default='99.99')