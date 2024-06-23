from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UPDATEINFO, DETAILTUTOR, PAYMENTRECORD
from django.db.models.signals import pre_save
from .dll import verify, sign, keygen
# from django.db.models import Q 
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

@receiver(pre_save, sender=PAYMENTRECORD)
def validate_payment_record(sender, instance, **kwargs):
    if instance.pk is not None:  # Check if the record already exists
        old_record = sender.objects.get(pk=instance.pk)
        changes = []
        
        # Compare fields to check for changes
        if old_record.user != instance.user:
            changes.append('User')
        if old_record.order_id != instance.order_id:
            changes.append('Order ID')
        if old_record.amount != instance.amount:
            changes.append('Amount')
        if old_record.order_desc != instance.order_desc:
            changes.append('Order Description')
        if old_record.transaction_no != instance.transaction_no:
            changes.append('Transaction Number')
        if old_record.response_code != instance.response_code:
            changes.append('Response Code')
        if old_record.publickey != instance.publickey:
            changes.append('Public Key')
        if old_record.signature != instance.signature:
            changes.append('Signature')
        if old_record.message != instance.message:
            changes.append('Message')

        if changes:
            message = f"{instance.user}|{instance.order_id}|{instance.amount}|{instance.order_desc}|{instance.transaction_no}|{instance.response_code}"
            message = message.encode('utf-8') if isinstance(message, str) else message

            signature = instance.signature.encode('utf-8') if isinstance(instance.signature, str) else instance.signature
            publickey = instance.publickey.encode('utf-8') if isinstance(instance.publickey, str) else instance.publickey

            if verify(message, signature, publickey) == True:
                instance.status = "Valid"
            else:
                modified_fields = ", ".join(changes)
                instance.status = f"Invalid. The following fields have been modified: {modified_fields}"