

brew install python3 
#Then, the pip or pip3 is installed automatically

sudo pip3 install virtualenv
#
create root folder, cd into the foler & do cmd:  virtualenv .
source bin/activate; 
do: pip install django; 
do; pip freeze; 
mkdir apps

cd into apps; django-admin.py startproject todo_app (MAIN)

from todo_app (where you have manage.py) do
  python manage.py runserver. 
   python manage.py migrate
python manage.py createsuperuser

manage.py startapp todo_list

in todo list edit models to create databases.
3 step to create a db
1. create a class in models.py 
    from django.db import models

# Create your models here.
class List (models.Model):
    items = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# define how it is listed in the admin section
    def __str__(self):
        return self.items + ' | '+ str(self.completed)

2. create a migration: python manage.py makemigrations 
3. pushing the migration into the database :  python mange.py migrate 

Register db to show up in admin page in admin.py (in todo_list):
    from .models import List 

to use static file like css, images js. create static folder in the root(where manage.py is); the goto settings.py in the main app add to the bottom:
STATICFILES_DIRS =[
   os.path.join(BASE_DIR, 'static'),
] (edited)