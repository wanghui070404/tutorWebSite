from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# class TUTOR(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     subject = models.CharField(max_length=50, null=False)
#     Optimistic = models.IntegerField(default=0, null=True, blank=True)
#     Introduction = models.CharField(max_length=300, null=False)
#     Proficiency = models.CharField(max_length=200, null=False)
#     image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.name
#     @property
#     def ImageURL(self):
#         try: 
#             url = self.image.url
#         except:
#             url = ''
#         return url
    
class DETAILTUTOR(models.Model):
    status = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=6, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=50, null=False)
    certificate = models.ImageField(null=False, blank=False, upload_to='img/')
    avatar = models.ImageField(null=False, blank=False, upload_to='img_avatar/')
    video = models.FileField(null=True, blank=True, upload_to='videos/')
    subject1 = models.CharField(max_length=10, null=False)
    subject2 = models.CharField(max_length=10, null=True)
    subject3 = models.CharField(max_length=10, null=True)
    Introduction = models.CharField(max_length=600, null=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url

class UPDATEAVATAR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(null=False, blank=False, upload_to='updateimg/')

    def __str__(self):
        return str(self.user)

class UPDATEINFO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    school = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=6, null=False)
    date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.user)
    
class COUNSELING(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    form = models.CharField(max_length=15, null=False)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    subject = models.CharField(max_length=10, null=False)
    province = models.CharField(max_length=20, null=False)
    district = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.user)
    

#Chat
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
