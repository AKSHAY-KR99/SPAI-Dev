from django.contrib import admin
from .models import (GalleryManagement, User,
                     UserDetailModel, GalleryImage, PaymentModel, EventManagement, LifeMembers)

# Register your models here.

admin.site.register(GalleryManagement)
admin.site.register(User)
admin.site.register(UserDetailModel)
admin.site.register(GalleryImage)
admin.site.register(PaymentModel)
admin.site.register(EventManagement)
admin.site.register(LifeMembers)
