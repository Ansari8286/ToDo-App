from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from app.models import ToDo, DeleteItem


@receiver(pre_delete, sender=ToDo)
def before_delete(sender, instance, **kwargs):
    name = instance.name
    file = instance.file
    DeleteItem.objects.create(name=name, file=file)
