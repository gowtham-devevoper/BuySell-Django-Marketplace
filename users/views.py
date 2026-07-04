from django.shortcuts import render, redirect

from .forms import *

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib import messages

from django.contrib.auth.models import User

from .models import UserProfile, OTP

from django.core.mail import send_mail

from django.conf import settings

import random

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            # Email Exists Check

            existing_user = User.objects.filter(
                email=email
            ).first()

            if existing_user:

                if existing_user.is_active:

                    messages.error(
                        request,
                        "Email already exists"
                    )

                    return redirect(
                        'register'
                    )

                else:

                    existing_user.delete()

            # Mobile Exists Check

            if UserProfile.objects.filter(
                mobile=mobile
            ).exists():

                messages.error(
                    request,
                    "Mobile number already exists"
                )

                return redirect(
                    'register'
                )

            # Create User

            user = form.save(
                commit=False
            )

            user.username = email

            user.email = email

            user.first_name = (
                form.cleaned_data['first_name']
            )

            user.last_name = (
                form.cleaned_data['last_name']
            )

            user.is_active = False

            user.set_password(
                form.cleaned_data['password1']
            )

            user.save()

            # Save Mobile

            UserProfile.objects.create(
                user=user,
                mobile=mobile
            )

            # Delete old OTP

            OTP.objects.filter(
                user=user
            ).delete()

            # Generate OTP

            otp = str(
                random.randint(
                    100000,
                    999999
                )
            )

            OTP.objects.create(
                user=user,
                otp=otp
            )

            # Send OTP

            send_mail(
                "BuySell OTP Verification",
                f"Your OTP is {otp}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            request.session[
                'user_id'
            ] = user.id

            messages.success(
                request,
                "OTP sent to your email"
            )

            return redirect(
                'verify_otp'
            )

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


# =========================
# VERIFY OTP
# =========================

def verify_otp(request):

    user_id = request.session.get(
        'user_id'
    )

    if not user_id:

        return redirect(
            'register'
        )

    try:

        user = User.objects.get(
            id=user_id
        )

    except User.DoesNotExist:

        return redirect(
            'register'
        )

    otp_obj = OTP.objects.filter(
        user=user
    ).last()

    if request.method == "POST":

        entered_otp = request.POST.get(
            'otp'
        )

        if not otp_obj:

            messages.error(
                request,
                "OTP not found"
            )

            return redirect(
                'verify_otp'
            )

        # OTP Expired

        if otp_obj.is_expired():

            otp_obj.delete()

            messages.error(
                request,
                "OTP expired. Click Resend OTP."
            )

            return redirect(
                'verify_otp'
            )

        # OTP Match

        if entered_otp == otp_obj.otp:

            user.is_active = True

            user.save()

            otp_obj.delete()

            messages.success(
                request,
                "Registration Successful"
            )

            return redirect(
                'login'
            )

        else:

            messages.error(
                request,
                "Invalid OTP"
            )

    return render(
        request,
        'accounts/verify_otp.html'
    )


# =========================
# RESEND OTP
# =========================

def resend_otp(request):

    user_id = request.session.get(
        'user_id'
    )

    if not user_id:

        return redirect(
            'register'
        )

    try:

        user = User.objects.get(
            id=user_id
        )

    except User.DoesNotExist:

        return redirect(
            'register'
        )

    OTP.objects.filter(
        user=user
    ).delete()

    otp = str(
        random.randint(
            100000,
            999999
        )
    )

    OTP.objects.create(
        user=user,
        otp=otp
    )

    send_mail(
        "BuySell OTP Verification",
        f"Your new OTP is {otp}",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
    )

    messages.success(
        request,
        "New OTP sent successfully"
    )

    return redirect(
        'verify_otp'
    )


# =========================
# LOGIN
# =========================

def login_user(request):

    if request.method == "POST":

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user:

            if user.is_active:

                login(
                    request,
                    user
                )

                return redirect(
                    'home'
                )

            else:

                request.session[
                    'user_id'
                ] = user.id

                messages.warning(
                    request,
                    "Please verify OTP first"
                )

                return redirect(
                    'verify_otp'
                )

        else:

            messages.error(
                request,
                "Invalid Email or Password"
            )

    return render(
        request,
        'accounts/login.html'
    )


# =========================
# LOGOUT
# =========================

def logout_user(request):

    logout(request)

    return redirect(
        'login'
    )



@login_required
def my_profile(request):

    profile = get_object_or_404(
    UserProfile,
    user=request.user
)
    return render(
        request,'accounts/my_profile.html',{'profile':profile}
    )



@login_required
def edit_profile(request):

    profile = UserProfile.objects.get(
        user=request.user
    )

    if request.method == "POST":

        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            request.user.first_name = request.POST.get(
                'first_name'
            )

            request.user.last_name = request.POST.get(
                'last_name'
            )

            request.user.email = request.POST.get(
                'email'
            )

            request.user.save()

            # Delete Photo

            if form.cleaned_data.get(
                'delete_photo'
            ):

                if profile.profile_photo:

                    profile.profile_photo.delete(
                        save=False
                    )

                    profile.profile_photo = None

            form.save()

            messages.success(
                request,
                "Profile Updated Successfully"
            )

            return redirect(
                'my_profile'
            )

    else:

        form = EditProfileForm(
            instance=profile
        )

    return render(
        request,
        'accounts/edit_profile.html',
        {
            'form': form,
            'profile': profile
        }
    )

