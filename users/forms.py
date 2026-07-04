from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    email = forms.EmailField(
        label="Email Address"
    )

    mobile = forms.CharField(
        label="Mobile Number", max_length=10
    )

    password1 = forms.CharField(
        label="Create Password",
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput()
    )


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile',
            'password1',
            'password2'
        ]


class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=100
    )

    last_name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    delete_photo = forms.BooleanField(
        required=False,
        label="Delete Current Photo"
    )

    class Meta:

        model = UserProfile

        fields = [
            'mobile',
            'profile_photo'
        ]