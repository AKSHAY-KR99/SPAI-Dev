import os

from django.db import models


class GalleryManagement(models.Model):
    image = models.ImageField(upload_to='SPAI/images/gallery')
    upload_date = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Delete the image file from the local directory
        os.remove(self.image.path)
        super(GalleryManagement, self).delete(*args, **kwargs)

    def __str__(self):
        return self.image_name
