from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Client


@receiver(post_save, sender=Client)
def addertorefered(sender, instance, created, **kwargs):
    print("Signal!{0} pk:{1}".format(instance, instance.pk))
    if instance.referer and instance not in instance.referer.refered.all():
        print("signal pushed")
        referer = Client.objects.get(pk=instance.referer.pk)
        transaction.on_commit(func=lambda: referer.refered.add(instance))
