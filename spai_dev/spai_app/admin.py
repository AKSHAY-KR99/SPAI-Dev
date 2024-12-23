from django.contrib import admin
from .models import (GalleryManagement, User,
                     UserDetailModel, GalleryImage, PaymentModel, EventManagement, LifeMembers, InternshipApplication,
                     Manuscript, Author, EventDocumentModel)


# Register your models here.


admin.site.register(GalleryManagement)
admin.site.register(User)
admin.site.register(UserDetailModel)
admin.site.register(GalleryImage)
admin.site.register(PaymentModel)
admin.site.register(EventManagement)
admin.site.register(LifeMembers)
admin.site.register(InternshipApplication)
admin.site.register(Manuscript)
admin.site.register(Author)
admin.site.register(EventDocumentModel)
