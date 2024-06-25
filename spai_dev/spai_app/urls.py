

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('members/',views.members,name="members"),
    path('gallery/',views.gallery,name="gallery"),
    path('accademics/',views.accademics,name="accademics"),
    path('news/',views.news,name="news"),
    path('publications/',views.publications,name="publications"),
    path('search/',views.search,name="search"),
    path('add_image_template/',views.add_image_template,name="add_image_template"),
    path('login/', views.Login.as_view(), name='login'),

    #path('gallery/', views.GalleryManagementView.as_view(), name='gallery')
]


