from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup_in/',views.signup_in , name='signup_in'),
    path('timgiasu/',views.find , name='find'),
    path('giasu/',views.tutor ,name='tutor'),
    path('signout/', views.signout, name='signout'),
    path('timgiasu/info/', views.info, name='info'),
    path('Taikhoancuatoi/', views.personal_account, name='personal_account'),
    #reset password
    path('signup_in/reset_pass/', views.reset_pass, name='reset_pass'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app/reset_password_mail.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/reset_password.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app/reset_password_complete.html"), name="password_reset_complete"),

    #khi gửi form thành công
    path('success/', views.success, name='success_page'),
    path('success_form/', views.success, name='success_page_2'),
    #savedata
    path('save_data/', views.save_data, name='save_data'),
    #update avatar
    path('update_avatar/', views.update_avatar, name='update_avatar'),
    #update info
    path('update_info/', views.update_info, name='update_info'),
    #change password
    path('change_password/', views.change_password, name='change_password'),
    #savecounseling
    path('save_counseling/', views.save_counseling, name='save_counseling'),
    
    #

    #Chat
    path('timgiasu/home_chat/', views.home_chat, name='home_chat'),
    path('<str:room>/', views.room_chat, name='room_chat'),
    path('timgiasu/home_chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
    #like
    path('post/<int:pk>/like', views.like, name='like'),
    #dislike
    path('post/<int:pk>/dislike', views.dislike, name='dislike'),
]