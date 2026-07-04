from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


# =========================
# USER PROFILE
# =========================

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    mobile = models.CharField(
        max_length=10,
        unique=True
    )

    profile_photo = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )
    is_premium = models.BooleanField(
        default=False
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0
    )

    total_views = models.PositiveIntegerField(
        default=0
    )

    last_seen = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.user.email


# =========================
# OTP MODEL
# =========================

class OTP(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    otp = models.CharField(
        max_length=6
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def is_expired(self):

        return timezone.now() > (
            self.created_at +
            timedelta(minutes=5)
        )

    def __str__(self):

        return f"{self.user.email} - {self.otp}"