from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import DETAILTUTOR
from .models import UPDATEAVATAR
from .models import UPDATEINFO
from .models import COUNSELING, LOADVIDEO
from .models import Room, Message
from .form import CommentForm
from django.db.models import Q  
# from .models import Room, Message
from django.http import HttpResponse, JsonResponse
#PAYMENT
import hashlib
import hmac
import json
import urllib
import urllib.parse
import urllib.request
import random
import requests
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
#from django.utils.http import urlquote
from app1.models import PaymentForm
from app1.vnpay import vnpay
from django.contrib import admin
from .dll import sign, verify, keygen
# Create your views here.

def signup_in(request):
    if request.method == "POST":
        if "register" in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if User.objects.filter(username=username).exists():
                messages.error(request, "Tên người dùng đã tồn tại!")
                return redirect('signup_in')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email đã tồn tại!")
                return redirect('signup_in')
            if pass1 == pass2:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.save()

                messages.success(request, "Đăng ký thành công!")
                return redirect('signup_in')     
            else:
                messages.error(request, "Đăng ký không thành công!")
                
          
        elif "login" in request.POST:
            usernamel = request.POST['usernamel']
            passl = request.POST['passl']

            user = authenticate(username = usernamel, password = passl)

            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    user_not_login = "none"
                    user_login = "block"
                else:
                    user_not_login = "block"
                    user_login = "none"
                context = {'user_login': user_login, 'user_not_login': user_not_login}
                return redirect('home')

            else: 
                messages.error(request, "Lỗi đăng nhập! Tên tài khoản hoặc mật khẩu sai!")
                return redirect('signup_in')
    return render(request, "app/login.html")


def signout(request):
    logout(request)
    return redirect('signup_in')

    
# def signup(request):
#     if request.method == "POST":
#         usernamel = request.POST['usernamel']
#         passl = request.POST['passl']

#         user = authenticate(username = usernamel, password = passl)

#         if user is not None:
#             login(request, user)
#             return render(request, "app/homepage.html")

#         else: 
#             messages.error(request, "Wrong!")
#             return render(request, 'app/login.html')
            

def home(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None  # Set avatar to None for unauthenticated users

    # Render template với context
    context = {'avatar': avatar,'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/homepage.html', context)


def find(request):
    tutors = DETAILTUTOR.objects.all()
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    context = {'avatar': avatar,'tutors': tutors, 'user_login': user_login, 'user_not_login': user_not_login}  
    return render(request, 'app/Timkiem.html', context)



#####timkiem-filter section#####
def filter_Name(request):
    tag = 'Tên gia sư'
    tutors = DETAILTUTOR.objects.all().order_by('name')
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    context = {'avatar': avatar,'tutors': tutors, 'tag': tag, 'user_login': user_login, 'user_not_login': user_not_login}  
    return render(request, 'app/Timkiem_Filtered.html', context)
def filter_subject(request):
    tag = 'Môn'
    tutors = DETAILTUTOR.objects.all().order_by('subject1')
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    context = {'avatar': avatar,'tutors': tutors, 'tag': tag, 'user_login': user_login, 'user_not_login': user_not_login}  
    return render(request, 'app/Timkiem_Filtered.html', context)

def filter_School(request):
    tag = 'Trường'
    tutors = DETAILTUTOR.objects.all().order_by('-school')
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    context = {'avatar': avatar,'tutors': tutors, 'tag': tag, 'user_login': user_login, 'user_not_login': user_not_login}  
    return render(request, 'app/Timkiem_Filtered.html', context)

def tutor_search(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    query = request.GET.get('tim', '')
    tutors = DETAILTUTOR.objects.filter(Q(name__icontains=query) |
                                   Q(subject1__icontains=query) |
                                   Q(Introduction__icontains=query) |    
                                   Q(school__icontains=query))
                                   
    context = {'avatar': avatar,'tutors': tutors, 'user_login': user_login, 'user_not_login': user_not_login}  
    return render(request, 'app/Timkiem_Filtered.html', context)

#####timkiem-filter section#####

def tutor(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    # Render template với context
    context = {'avatar': avatar,'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/tutor.html', context)
#information of a tutor when you click on profile button
def info(request,pk):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
        return redirect('require_login')
    product = get_object_or_404(DETAILTUTOR,pk = pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user,tutor=product)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(request.path)
    # Render template với context
    context = {'avatar':avatar, 'user_login': user_login, 'user_not_login': user_not_login,'product':product,'form':form}
    return render(request, 'app/tutor_profile.html', context)

def comment_del(request, tutor, comment):
    product = get_object_or_404(DETAILTUTOR, pk=tutor)
    comment = get_object_or_404(Comment, tutor=product, id=comment)

    # Kiểm tra xem người dùng hiện tại có phải là tác giả của comment không
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment has been deleted.')
    else:
        messages.error(request, 'You do not have permission to delete this comment.')

    return redirect('info', pk=tutor)

#Tài nguyên học
def academic_resource(request):
    sources = LOADVIDEO.objects.all()
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
        # Truy vấn dữ liệu từ bảng UPDATEAVATAR
        try:
            avatar = UPDATEAVATAR.objects.get(user=request.user)
        except UPDATEAVATAR.DoesNotExist:
            avatar = None
    else:
        user_not_login = "block"
        user_login = "none"
        avatar = None
    # Render template với context
    context = {'avatar':avatar, 'user_login': user_login, 'user_not_login': user_not_login, 'sources': sources}
    return render(request, 'app/TNHOC.html', context)
    

def reset_pass(request):
    return render(request, 'app/reset_password.html')
def personal_account(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
    else:
        user_not_login = "block"
        user_login = "none"

    try:
        update_avatar = UPDATEAVATAR.objects.get(user=request.user)
    except UPDATEAVATAR.DoesNotExist:
        update_avatar = None  # hoặc cung cấp một giá trị mặc định hoặc xử lý tương ứng
    # Truy vấn dữ liệu từ bảng UPDATEAVATAR
    try:
        avatar = UPDATEAVATAR.objects.get(user=request.user)
    except UPDATEAVATAR.DoesNotExist:
        avatar = None
    # Render template với context

    context = {'avatar':avatar,'update_avatar': update_avatar, 'user_login': user_login, 'user_not_login': user_not_login}

    return render(request, 'app/Personal-account.html', context)


# load dữ liệu từ form lên database

@login_required(login_url='require_login')
def save_data(request):
        if request.method == 'POST':
            if request.user.is_authenticated:
            # Lấy dữ liệu từ POST request
                current_user = request.user
                user = current_user
                name = request.POST.get('name')
                sex = request.POST.get('sex')
                phone_number = request.POST.get('phone')
                address = request.POST.get('current-address')
                school = request.POST.get('school')
                avatar = request.FILES.get('avatar')
                video = request.FILES.get('video')
                certificate = request.FILES.get('certificate')
                subject1 = request.POST.get('subject1')
                subject2 = request.POST.get('subject2')
                subject3 = request.POST.get('subject3')
                Introduction = request.POST.get('introduction') 
                en = DETAILTUTOR(user=user, name=name, sex=sex, phone_number=phone_number, address=address, school=school, avatar=avatar, video=video, certificate=certificate, subject1=subject1, subject2=subject2, subject3=subject3, Introduction=Introduction)
                # Tạo một đối tượng mới từ model và lưu vào cơ sở dữ liệu
                # detailtutor = DETAILTUTOR.objects.create(name=name, sex=sex, phone_number=phone_number, address=address, school=school, certificate=certificate, subject1=subject1, subject2=subject2, subject3=subject3, Introduction=Introduction)
                en.save()
                # Sau khi lưu dữ liệu, bạn có thể thực hiện các thao tác khác như chuyển hướng người dùng đến một trang khác
                return redirect('success_page')
            else:
                return redirect('signup_in')


@login_required
def update_info(request):
    if request.method == 'POST':
        update_name = request.POST['name']       
        update_phone = request.POST['phone']
        update_school = request.POST['school']
        update_sex = request.POST['sex']
        uploaded_img = request.FILES['avatar']
        update_introduction = request.POST['introduction']
        update_current_address = request.POST['current-address']


        try:
            update_info = UPDATEINFO.objects.get(user=request.user)
            update_info.name = update_name
            update_info.phone_number = update_phone
            update_info.school = update_school
            update_info.sex = update_sex
            update_info.avatar = uploaded_img
            update_info.Introduction = update_introduction
            update_info.address = update_current_address
            update_info.status = 0
        except UPDATEINFO.DoesNotExist:
            update_info = UPDATEINFO(user=request.user, status=0 ,name=update_name, phone_number=update_phone, school=update_school, sex=update_sex, address=update_current_address, avatar=uploaded_img, Introduction=update_introduction) #date=update_date,
        
        update_info.save()
        return redirect('personal_account')
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "block"
    else:
        user_not_login = "block"
        user_login = "none"
    context = {'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/Personal-account.html', context)
        
#Khi gửi form thành công
def success(request):
    return render(request, 'app/successpage.html')
def success2(request):
    return render(request, 'app/successpage2.html')
def require_login(request):
    return render(request, 'app/require-login.html')


#Update avatar
# def update_avatar(request):
#     if request.method == 'POST':
#         current_user = request.user
#         user = current_user
#         avatar = request.FILES.get('avatar')
#         en = UPDATEAVATAR(user=user, avatar=avatar)
#         en.save()
#     if request.user.is_authenticated:
#         user_not_login = "none"
#         user_login = "block"
#     else:
#         user_not_login = "block"
#         user_login = "none"
#     context = {'user_login': user_login, 'user_not_login': user_not_login}
#     return render(request, 'app/Personal-account.html', context)

@login_required
def update_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        uploaded_img = request.FILES['avatar']

        try:
            avatar_img = UPDATEAVATAR.objects.get(user=request.user)
            avatar_img.avatar = uploaded_img
        except UPDATEAVATAR.DoesNotExist:
            avatar_img = UPDATEAVATAR(user=request.user, avatar=uploaded_img)
        
        avatar_img.save()       
        return redirect('personal_account')
   
    return render(request, 'app/Personal-account.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_user = request.user
        old_password = request.POST.get('old-pass')
        new_password = request.POST.get('new-pass')


        #Kiểm tra mật khẩu cũ 
        if not current_user.check_password(old_password):
            messages.error(request, 'Mật khẩu cũ sai!. Vui lòng thử lại!')
            return redirect('personal_account')
        
        #Thay đổi mật khẩu
        current_user.password = make_password(new_password)
        current_user.save()

        # Cập nhật session auth hash để người dùng vẫn đăng nhập sau khi thay đổi mật khẩu
        update_session_auth_hash(request, current_user)
        messages.success(request, 'Mật khẩu của bạn đã được cập nhật!')
        return redirect('personal_account')

    return render(request, 'app/Personal-account.html')

@login_required(login_url='require_login')  
def save_counseling(request):
    if request.method == 'POST':
        current_user = request.user
        user = current_user
        form = request.POST.get('form')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        subject = request.POST.get('subject')
        province = request.POST.get('province')
        district = request.POST.get('district')
        address = request.POST.get('address')
        description = request.POST.get('description')

        en = COUNSELING(user=user, form=form, name=name, phone_number=phone_number, subject=subject, province=province, district=district, address=address, description=description)
        # Tạo một đối tượng mới từ model và lưu vào cơ sở dữ liệu
        # detailtutor = DETAILTUTOR.objects.create(name=name, sex=sex, phone_number=phone_number, address=address, school=school, certificate=certificate, subject1=subject1, subject2=subject2, subject3=subject3, Introduction=Introduction)
        en.save()
        # Sau khi lưu dữ liệu, bạn có thể thực hiện các thao tác khác như chuyển hướng người dùng đến một trang khác
        return redirect('success_page_2')
    return render(request, 'app/tutor.html')


#CHAT   
def home_chat(request):
    if request.user.is_authenticated:
        try:
            username = UPDATEINFO.objects.get(user=request.user)
        except UPDATEINFO.DoesNotExist:
            username = None
        context = {'username':username}
        return render(request, 'app/home_chat.html', context)
    else:
        return redirect('require_login')

def room_chat(request, room):
    try:
        room_details = Room.objects.get(name=room)
        username = request.GET.get('username')
        return render(request, 'app/room_chat.html', {
            'username': username,
            'room': room,
            'room_details': room_details
        })
    except Room.DoesNotExist:
        # Xử lý khi phần tử không tồn tại
        price = request.GET.get('price')
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = amount * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code

            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            print(vnpay_payment_url)
            return redirect(vnpay_payment_url)
        else:
            print("Form input not validate")
    else:
        return render(request, "payment/payment.html", {"title": "Thanh toán", "price": price})

def checkview(request):
    room = request.POST['room_name']
    username = request.POST.get('username', '')

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id).values('user', 'value')
    return JsonResponse({"messages":list(messages.values())})


#PAYMENT
def index(request):
    return render(request, "payment/index.html", {"title": "Danh sách demo"})


def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


def payment(request):
    price = request.GET.get('price')
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = amount * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code

            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            print(vnpay_payment_url)
            return redirect(vnpay_payment_url)
        else:
            print("Form input not validate")
    else:
        return render(request, "payment/payment.html", {"title": "Thanh toán", "price": price})


def payment_ipn(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            # Your code here
            firstTimeUpdate = True
            totalamount = True
            if totalamount:
                if firstTimeUpdate:
                    if vnp_ResponseCode == '00':
                        print('Payment Success. Your code implement here')
                    else:
                        print('Payment Error. Your code implement here')

                    # Return VNPAY: Merchant update success
                    result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    # Already Update
                    result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
            else:
                # invalid amount
                result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
        else:
            # Invalid Signature
            result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result





@login_required
def payment_return(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        user = request.user
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']

     
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            if vnp_ResponseCode == "00":
                #Sign the data
                message = f"{user}|{order_id}|{amount}|{order_desc}|{vnp_TransactionNo}|{vnp_ResponseCode}"
                message = message.encode('utf-8')
                privatekey = 'C:\\Savekey\\private.bin'
                privatekey = privatekey.encode('utf-8')
                publickey = keygen(privatekey)
                signature = sign(message, privatekey)
              
                # with open('C:\\Savekey\\public_key.bin', 'w') as f:
                #     f.write(f"Public Key: {publickey}\n")

                # with open('C:\\Savekey\\signature.bin', 'w') as f:
                #     f.write(f"Signature: {signature}\n")
                status = ''
                
                if verify(message, signature, publickey) == True:
                    status = "Valid"
                else: 
                    status = "Invalid"
                payment = PAYMENTRECORD.objects.create(
                    user = user,
                    order_id = order_id,
                    amount = amount,
                    order_desc = order_desc,
                    transaction_no = vnp_TransactionNo,
                    response_code = vnp_ResponseCode,
                    publickey = publickey,
                    signature = signature,
                    message = message,
                    status = status,
                )

                payment.save()           



                return render(request, "payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                               "result": "Thành công", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
            else:
                return render(request, "payment/payment_return.html", {"title": "Kết quả thanh toán",
                                                               "result": "Lỗi", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
        else:
            return render(request, "payment/payment_return.html",
                          {"title": "Kết quả thanh toán", "result": "Lỗi", "order_id": order_id, "amount": amount,
                           "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
                           "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum"})
    else:
        return render(request, "payment/payment_return.html", {"title": "Kết quả thanh toán", "result": ""})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

n = random.randint(10**11, 10**12 - 1)
n_str = str(n)
while len(n_str) < 12:
    n_str = '0' + n_str


def query(request):
    if request.method == 'GET':
        return render(request, "payment/query.html", {"title": "Kiểm tra kết quả giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_Version = '2.1.0'

    vnp_RequestId = n_str
    vnp_Command = 'querydr'
    vnp_TxnRef = request.POST['order_id']
    vnp_OrderInfo = 'kiem tra gd'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode,
        vnp_TxnRef, vnp_TransactionDate, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, "payment/query.html", {"title": "Kiểm tra kết quả giao dịch", "response_json": response_json})

def refund(request):
    if request.method == 'GET':
        return render(request, "payment/refund.html", {"title": "Hoàn tiền giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_RequestId = n_str
    vnp_Version = '2.1.0'
    vnp_Command = 'refund'
    vnp_TransactionType = request.POST['TransactionType']
    vnp_TxnRef = request.POST['order_id']
    vnp_Amount = request.POST['amount']
    vnp_OrderInfo = request.POST['order_desc']
    vnp_TransactionNo = '0'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_CreateBy = 'user01'
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode, vnp_TransactionType, vnp_TxnRef,
        vnp_Amount, vnp_TransactionNo, vnp_TransactionDate, vnp_CreateBy, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_Amount": vnp_Amount,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_TransactionType": vnp_TransactionType,
        "vnp_TransactionNo": vnp_TransactionNo,
        "vnp_CreateBy": vnp_CreateBy,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, "payment/refund.html", {"title": "Kết quả hoàn tiền giao dịch", "response_json": response_json})