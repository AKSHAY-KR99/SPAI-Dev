from django.contrib import admin
from .models import GalleryManagement, User, UserDetailModel

# Register your models here.

admin.site.register(GalleryManagement)
admin.site.register(User)
admin.site.register(UserDetailModel)
