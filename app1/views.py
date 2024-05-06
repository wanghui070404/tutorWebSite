from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import LikeForm
from django.conf import settings
from .models import DETAILTUTOR
from .models import UPDATEAVATAR
from .models import UPDATEINFO
from .models import COUNSELING
from django.shortcuts import get_object_or_404
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.

def signup_in(request):
    if request.method == "POST":
        if "register" in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.save()

                messages.success(request, "Successfully!")
                return redirect('signup_in')     
            else:
                messages.error(request, "Wrong!")
                
          
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
                messages.error(request, "Wrong!")
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
def info(request):
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
    context = {'avatar':avatar, 'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/tutor_profile.html', context)

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

@login_required
def save_data(request):
    if request.method == 'POST':
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
    return render(request, 'app/tutor.html')

@login_required
def update_info(request):
    if request.method == 'POST' and request.POST.get('name') and request.POST.get('phone') and request.POST.get('school') and request.POST.get('sex') and request.POST.get('date') and request.POST.get('current-address'):
        update_name = request.POST['name']       
        update_phone = request.POST['phone']
        update_school = request.POST['school']
        update_sex = request.POST['sex']
        update_date = request.POST['date']
        update_current_address = request.POST['current-address']

        try:
            update_info = UPDATEINFO.objects.get(user=request.user)
            update_info.name = update_name
            update_info.phone_number = update_phone
            update_info.school = update_school
            update_info.sex = update_sex
            update_info.date = update_date
            update_info.address = update_current_address
        except UPDATEINFO.DoesNotExist:
            update_info = UPDATEINFO(user=request.user, name=update_name, phone_number=update_phone, school=update_school, sex=update_sex, date=update_date, address=update_current_address)
        
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

@login_required
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
    try:
        username = UPDATEINFO.objects.get(user=request.user)
    except UPDATEINFO.DoesNotExist:
        username = None
    context = {'username':username}
    return render(request, 'app/home_chat.html', context)

def room_chat(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'app/room_chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

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


def like_tutor(request):
    if request.method == 'POST':
        tutor_id = request.POST.get('tutor_id')
        room = get_object_or_404(Room, tutor_id=tutor_id)  # Truy vấn Room với tutor_id
        # Xử lý logic tăng số lượt like của room ở đây
        room.likes += 1
        room.save()
        return JsonResponse({'status': 'success', 'like_count': room.likes})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})