# HOW TO START A NEW DJANGO PROJECT
## _Command line:_

__Go to the Script folder to activate the virtual machine__

    $ cd Scripts\
 

 __Activate the virtual machine by typing__

    $ .\activate


__Back up one folder__

    $cd ..\


__Create a new folder for the new project__

    $ mkdir [project_name] (OPTINAL)


__Go to the project folder__
    
    $ cd ..\[project_name] (OPTIONAL)


__Start the django project__

    $ django-admin.exe startproject [project_name]


__Go to the project folder__
    
    $ cd [project_name]


__Go to the migrate the DB to the project__
    
    $ python manage.py migrate


__Start the django server__

    $ python manage.py runserver

----------
## the project server is already up from this point
-----------

__Create super user__

    $ python manage.py createsuperuser


__Create app for the project__
    
    $ python manage.py startapp pages


## __How to create a new app:__

__On the PowerShell type the following commands:__

    $ python manage.py startapp pages


## __How to create a new model:__

__On [app_name]/'models.py' create a *Class* [model_name] with the following codes:__

    $ class Courses(models.Model):
        title       = models.CharField(max_length=120) 
        description = models.TextField(blank=True, null=True)
        price       = models.DecimalField(decimal_places=2, max_digits=1000, default=0.00)
        summary     = models.TextField(blank=False, null=True) 
        feature     = models.BooleanField() #null=True, default=True

__On [app_name]/'admin.py' import the following *Class* previously create on [app_name]/'models.py' by typing:__

    $ from .models import [class_name]

    $ admin.site.register(Courses)


## __Every time a new model is created or modified the following command line should be ran__

    $ python manage.py makemigrations

    $ python manage.py migrate




