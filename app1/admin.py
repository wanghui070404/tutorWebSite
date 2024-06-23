from django.contrib import admin
from .models import *
from .dll import verify, keygen, sign
from .views import payment_return
# Register your models here.
admin.site.register(DETAILTUTOR)
admin.site.register(UPDATEAVATAR)
admin.site.register(UPDATEINFO)
admin.site.register(COUNSELING)

# #Chat
admin.site.register(Room)
admin.site.register(Message)

# admin.site.register(PAYMENTRECORD)
admin.site.register(LOADVIDEO)
admin.site.register(Comment)


class PaymentRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('status',)  # Chỉ đọc trường 'status'
admin.site.register(PAYMENTRECORD, PaymentRecordAdmin)


# def verify_payment_record(modeladmin, request, queryset):
#     for record in queryset:
#         # Thực hiện xác minh
#         message = f"{record.user}|{record.order_id}|{record.amount}|{record.order_desc}|{record.transaction_no}|{record.response_code}"
#         message = message.encode('utf-8')
#         # privatekey = 'C:\\Savekey\\private1.bin'
#         # privatekey = privatekey.encode('utf-8')
#         # publickey = keygen(privatekey)
#         # signature = sign(message, privatekey)

#         publickey = record.publickey.encode('utf-8')
#         signature = record.signature.encode('utf-8')
#         print()

#         if verify(message, signature, publickey) == True:  
#             record.status = "Valid"
#         else:
#             record.status = "Invalid"
#         record.save()

#     modeladmin.message_user(request, "Các hóa đơn đã được xác minh.")

# verify_payment_record.short_description = "Xác minh các hóa đơn đã chọn"

# # Đăng ký hành động và cấu hình trang quản trị
# class PAYMENTRECORDAction(admin.ModelAdmin):
#     list_display = ('user', 'order_id', 'amount', 'status')
#     actions = [verify_payment_record]
#     readonly_fields = ('status',)

# admin.site.register(PAYMENTRECORD, PAYMENTRECORDAction)

