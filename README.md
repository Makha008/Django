# Django

#installer django 3.1.1
pip3 install Django==3.1.1

#créér le projet
django-admin startproject Tp_Django

#création de l'application
python3 manage.py startapp todo


#créer un model Task dans
models.py.


class Task(models.Model):
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.content

#ajout de de l'app todo dans INSTALLED_APPS 

INSTALLED_APPS = [
       'todo',
]

#créer des migrations correspondant à ces changements.
python manage.py makemigrations 

#pour appliquer ces modifications à la base de données.
python manage.py migrate 

#run le projet
python3 manage.py runserver

#créer un super user
python3 manage.py createsuperuser

#dans settings.py ajouter  "templates"
#dans templates
'DIRS': ["templates"],
