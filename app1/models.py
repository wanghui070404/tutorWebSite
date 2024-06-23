from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.conf import settings
from .dll import verify

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=6, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=50, null=False)
    certificate = models.ImageField(null=False, blank=False, upload_to='img/')
    avatar = models.ImageField(null=False, blank=False, upload_to='img_avatar/')
    video = models.FileField(null=True, blank=True, upload_to='videos/')
    subject1 = models.CharField(max_length=10, null=False)
    subject2 = models.CharField(max_length=10, null=True, blank=True)
    subject3 = models.CharField(max_length=10, null=True, blank=True)
    Introduction = models.CharField(max_length=700, null=False)

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
    status = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=6, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='updateimg/')
    address = models.CharField(max_length=100, null=True, blank=True)
    Introduction = models.CharField(max_length=700, null=True, blank=True)

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
    

# Chat
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
def verifynew(self, message, publickey, signature):
    publickey = self.publickey.encode('utf-8')
    return verify(message, publickey, signature)

class PAYMENTRECORD(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_desc = models.TextField()
    transaction_no = models.CharField(max_length=255)
    response_code = models.CharField(max_length=10)
    publickey = models.CharField(max_length=10000, null=True, blank=True)  
    signature = models.CharField(max_length=10000, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)


    

    # def verifynew(self, message, publickey, signature): 
    #     publickey = publickey.encode('utf-8')
    #     return verify(message, publickey, signature)
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.status = False
    #     super().save(*args, **kwargs)
    # payment_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    # bank_code = models.CharField(max_length=10)
    # card_type = models.CharField(max_length=20)
    # success = models.BooleanField(default=False)
    
    
class PaymentForm(forms.Form):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
    
class LOADVIDEO(models.Model):
    Toan10 = models.CharField(max_length=255, blank=True, null=True)
    Toan11 = models.CharField(max_length=255, blank=True, null=True)
    Toan12 = models.CharField(max_length=255, blank=True, null=True)
    Ly10 = models.CharField(max_length=255, blank=True, null=True)
    Ly11 = models.CharField(max_length=255, blank=True, null=True)
    Ly12 = models.CharField(max_length=255, blank=True, null=True)
    Hoa10 = models.CharField(max_length=255, blank=True, null=True)
    Hoa11 = models.CharField(max_length=255, blank=True, null=True)
    Hoa12 = models.CharField(max_length=255, blank=True, null=True)
    Van10 = models.CharField(max_length=255, blank=True, null=True)
    Van11 = models.CharField(max_length=255, blank=True, null=True)
    Van12 = models.CharField(max_length=255, blank=True, null=True)
    Anh10 = models.CharField(max_length=255, blank=True, null=True)
    Anh11 = models.CharField(max_length=255, blank=True, null=True)
    Anh12 = models.CharField(max_length=255, blank=True, null=True)
    urlToan10 = models.URLField(max_length=255, blank=True, null=True)
    urlToan11 = models.URLField(max_length=255, blank=True, null=True)
    urlToan12 = models.URLField(max_length=255, blank=True, null=True)
    urlLy10 = models.URLField(max_length=255, blank=True, null=True)
    urlLy11 = models.URLField(max_length=255, blank=True, null=True)
    urlLy12 = models.URLField(max_length=255, blank=True, null=True)
    urlHoa10 = models.URLField(max_length=255, blank=True, null=True)
    urlHoa11 = models.URLField(max_length=255, blank=True, null=True)
    urlHoa12 = models.URLField(max_length=255, blank=True, null=True)
    urlVan10 = models.URLField(max_length=255, blank=True, null=True)
    urlVan11 = models.URLField(max_length=255, blank=True, null=True)
    urlVan12 = models.URLField(max_length=255, blank=True, null=True)
    urlAnh10 = models.URLField(max_length=255, blank=True, null=True)
    urlAnh11 = models.URLField(max_length=255, blank=True, null=True)
    urlAnh12 = models.URLField(max_length=255, blank=True, null=True)

class Comment(models.Model):
    tutor = models.ForeignKey(DETAILTUTOR,on_delete=models.CASCADE,null=True,related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)