import re
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm
from .models import GalleryManagement, UserDetailModel, User,EventManagement, PaymentModel, InternshipApplication
from django import forms


class GalleryManagementForm(ModelForm):
    class Meta:
        model = GalleryManagement
        fields = ['image', 'image_name', 'description']


class EventManagementForm(ModelForm):
    class Meta:
        model = EventManagement
        fields = ['title', 'image', 'datetime', 'location', 'description', 'registration_link']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


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


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetailModel
        fields = ('degree', 'profession', 'institution', 'department', 'phone_number', 'alternate_number',
                  'alternate_mail', 'photo', 'specialized_in', 'research_interest')

    house_name = forms.CharField(max_length=255, label='House Name')
    street_name = forms.CharField(max_length=255, label='Street Name')
    city_name = forms.CharField(max_length=255, label='City Name')
    pin = forms.CharField(max_length=6, label='PIN')

    def __init__(self, user, *args, **kwargs):
        super(UserDetailForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(UserDetailForm, self).save(commit=False)
        instance.user = self.user

        # Merge address fields into a single string
        address = (f"{self.cleaned_data['house_name']}, {self.cleaned_data['street_name']}, "
                   f"{self.cleaned_data['city_name']}, PIN - {self.cleaned_data['pin']}")
        instance.address = address

        if commit:
            instance.save()
        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', 'Email does not exist')
                return cleaned_data

            if not check_password(password, user.password):
                self.add_error('password', 'Invalid password')
                return cleaned_data

        return cleaned_data


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ('transaction_id', 'reference_id', 'bank_name', 'payment_type', 'document')

    def __init__(self, user, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super(PaymentForm, self).save(commit=False)
        instance.user_info = self.user
        if commit:
            instance.save()
        return instance


class InternshipApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'college', 'university', 'department',
            'interest_area', 'location_preference', 'start_date', 'end_date',
            'qualification', 'course_name', 'passing_year', 'score'
        ]
        read_only_fields = ['apply_date', 'apply_date']
