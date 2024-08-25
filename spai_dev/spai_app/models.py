import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone


def user_detail_image_path(instance, filename):
    path = f'user_detail/{instance.user.slug_value}/image/{filename}'
    return path


def user_detail_payment_path(instance, filename):
    path = f'user_detail/{instance.user_info.slug_value}/payment/{instance.payment_type}/{filename}'
    return path


def generate_unique_slug():
    slug = slugify(get_random_string(length=32))
    unique_slug = slug
    num = 1
    while User.objects.filter(slug_value=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


class EventManagement(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='SPAI/images/Events')
    datetime = models.DateTimeField()  # Updated field to store both date and time
    location = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    registration_link = models.CharField(max_length=200, null=True, blank=True)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(EventManagement, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class GalleryManagement(models.Model):
    image = models.ImageField(upload_to='SPAI/images/gallery', null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    image_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    event = models.ForeignKey(EventManagement, on_delete=models.SET_NULL, null=True, blank=True)
    place = models.CharField(max_length=255, null=True)

    def delete(self, *args, **kwargs):
        # Delete the image file from the local directory
        os.remove(self.image.path)
        super(GalleryManagement, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.image_name)


class GalleryImage(models.Model):
    gallery = models.ForeignKey(GalleryManagement, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image {self.id} - {self.gallery.image_name}"

    def delete(self, *args, **kwargs):
        # Delete the image file from the local directory
        os.remove(self.image.path)
        super(GalleryImage, self).delete(*args, **kwargs)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Please provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("superuser should have is_staff field is true"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser should have is_superuser field is true"))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, verbose_name="email_address", unique=True)
    username = models.CharField(max_length=50, verbose_name="username", unique=True)
    first_name = models.CharField(max_length=50, verbose_name="first_name", null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name="last_name", null=True, blank=True)
    state = models.CharField(max_length=30, choices=settings.STATE_CHOICES, default="None", null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    user_role = models.PositiveSmallIntegerField(choices=settings.ROLE_CHOICES, blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    slug_value = models.SlugField(auto_created=True, blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin_approved = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.slug_value:
            self.slug_value = generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.email)


class UserDetailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_details')
    degree = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    institution = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    alternate_number = models.CharField(max_length=15, null=True, blank=True)
    alternate_mail = models.EmailField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to=user_detail_image_path, null=True, blank=True)
    specialized_in = models.CharField(max_length=50, null=True, blank=True)
    research_interest = models.CharField(max_length=50, null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.photo:
            os.remove(self.photo.path)
        super(UserDetailModel, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.user.email)


class PaymentModel(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_model')
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    reference_id = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    payment_reported_date = models.DateField(auto_now_add=True)
    payment_type = models.PositiveSmallIntegerField(choices=settings.PAYMENT_TYPE, blank=True, null=True)
    document = models.FileField(upload_to=user_detail_payment_path, null=True, blank=True)

    def __str__(self):
        return str(self.user_info)

    def delete(self, *args, **kwargs):
        if self.document:
            os.remove(self.document.path)
        super(PaymentModel, self).delete(*args, **kwargs)
