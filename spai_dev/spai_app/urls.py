

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('exe_members/',views.exe_members,name="exe_members"),
    path('history/',views.history,name="history"),
    path('about_members/',views.about_members,name="about_members"),
    path('v_and_m/',views.v_and_m,name="v_and_m"),
    path('members/',views.members,name="members"),
    path('membership/',views.membership,name="membership"),
    path('publications/',views.publications,name="publications"),
    path('editorial/',views.editorial,name="editorial"),
    path('journal/',views.journal,name="journal"),
    path('submit_paper/',views.submit_paper,name="submit_paper"),
    path('gallery/',views.gallery,name="gallery"),
    path('accademics/',views.accademics,name="accademics"),
    path('news/',views.news,name="news"),
    path('search/',views.search,name="search"),
    path('add_image_template/',views.add_image_template,name="add_image_template"),
    path('login/', views.Login.as_view(), name='login'),
    path('gallery/delete/<int:id>', views.GalleryUploadDelete.as_view(), name='galleryimagedelete')
]


