import re
from django.conf import settings
from django.forms import ModelForm
from .models import GalleryManagement
from django import forms
from .models import User


class GalleryManagementForm(ModelForm):
    class Meta:
        model = GalleryManagement
        fields = ['image', 'image_name', 'description']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'state')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")

        if not re.search("[A-Z]", password):
            raise forms.ValidationError("Password must contain at least one uppercase letter")

        if not re.search("[a-z]", password):
            raise forms.ValidationError("Password must contain at least one lowercase letter")

        if not re.search("[@#_!]", password):
            raise forms.ValidationError(
                "Password must contain at least one of the following special characters: @, #, _,!")

        return password

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if str(password) != str(confirm_password):
            raise forms.ValidationError("Passwords do not match")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.status = settings.USER_CREATED  # set default status
        user.user_role = 2  # set default user role
        user.admin_approved = False  # set default admin approval
        if commit:
            user.save()
        return user
