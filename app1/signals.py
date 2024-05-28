from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UPDATEINFO, DETAILTUTOR

@receiver(post_save, sender=UPDATEINFO)
def update_info_status_change(sender, instance, **kwargs):
    if instance.status != 0:  # Nếu status là True (1)
        try:
            detail = DETAILTUTOR.objects.get(user=instance.user)
        except DETAILTUTOR.DoesNotExist:
            detail = DETAILTUTOR(user=instance.user)

        detail.name = instance.name
        detail.phone_number = instance.phone_number
        detail.school = instance.school
        detail.sex = instance.sex
        # detail.date = instance.date
        detail.avatar = instance.avatar
        detail.address = instance.address
        detail.Introduction = instance.Introduction
        detail.save()
        instance.status = 0