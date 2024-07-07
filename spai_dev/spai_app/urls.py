from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('exe_members/', views.exe_members, name="exe_members"),
    path('history/', views.history, name="history"),
    path('about_members/', views.about_members, name="about_members"),
    path('v_and_m/', views.v_and_m, name="v_and_m"),
    path('members/', views.members, name="members"),
    path('membership/', views.membership, name="membership"),
    path('publications/', views.publications, name="publications"),
    path('editorial/', views.editorial, name="editorial"),
    path('journal/', views.journal, name="journal"),
    path('submit_paper/', views.submit_paper, name="submit_paper"),
    path('gallery/', views.gallery, name="gallery"),
    path('accademics/', views.accademics, name="accademics"),
    path('news/', views.news, name="news"),
    path('events/delete/<int:event_id>/', views.delete_event, name='event_delete'),
    path('search/', views.search, name="search"),
    path('eventadd/', views.eventadd, name="eventadd"),
    path('add_image_template/', views.add_image_template, name="add_image_template"),
    path('user_details/login/', views.user_login, name='login'),
    path('gallery/delete/<int:id>', views.GalleryUploadDelete.as_view(), name='galleryimagedelete'),
    path('user_details/', views.user_detail_upload, name='user_detail'),
    path('logout/', views.user_logout, name='logout'),
    path('user/details/<str:slug>', views.user_details_vew, name='individual_user_details')
]
