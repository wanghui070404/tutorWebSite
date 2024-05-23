from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DETAILTUTOR)
admin.site.register(UPDATEAVATAR)
admin.site.register(UPDATEINFO)
admin.site.register(COUNSELING)

# #Chat
admin.site.register(Room)
admin.site.register(Message)

admin.site.register(PAYMENTRECORD)
admin.site.register(LOADVIDEO)
admin.site.register(Comment)




