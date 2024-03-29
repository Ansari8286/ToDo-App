from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=400)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name

class DeleteItem(models.Model):
    name = models.CharField(max_length=400)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name
        