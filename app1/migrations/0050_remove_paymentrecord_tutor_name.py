# Generated by Django 5.0.3 on 2024-06-10 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0049_paymentrecord_tutor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentrecord',
            name='tutor_name',
        ),
    ]
