from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=400)
    disc = models.CharField(max_length=400)
    edit = models.CharField(max_length=400)
    is_verifed = models.BooleanField(default=False, null=True, blank=True)
   
    def __str__(self):
        return self.name

class DeleteItem(models.Model):
    name = models.CharField(max_length=400)
    disc = models.CharField(max_length=400)

    def __str__(self):
        return self.name
        