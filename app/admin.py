from django.contrib import admin
from .models import ToDo, DeleteItem
# Register your models here.
admin.site.register(ToDo)
admin.site.register(DeleteItem)
