from django.contrib import admin
from .models import Courses, OldCourses

# Register your models here.

admin.site.register(Courses)
admin.site.register(OldCourses)
