from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('register/',views.register,name='register'),
  path('verify-otp/',views.verify_otp,name='verify_otp'),
  path('login/',views.login_user,name='login'),
  path('logout/',views.logout_user,name='logout'),
  path('resend-otp/',views.resend_otp,name='resend_otp'),
  path('my-profile/',views.my_profile,name='my_profile'),
  path('edit-profile/',views.edit_profile,name='edit_profile'),
]