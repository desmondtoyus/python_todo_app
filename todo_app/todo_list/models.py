from django.db import models

# Create your models here.
class List (models.Model):
    items = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# define how it is listed in the admin section
    def __str__(self):
        return self.items + ' | '+ str(self.completed)