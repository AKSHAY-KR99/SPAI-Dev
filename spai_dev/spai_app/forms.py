from django.forms import ModelForm
from .models import GalleryManagement


class GalleryManagementForm(ModelForm):
    class Meta:
        model = GalleryManagement
        fields = ['image', 'image_name', 'description']
