from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('history/', views.history, name="history"),
    path('about_members/', views.about_members, name="about_members"),
    path('members/', views.members, name="members"),
    path('membership/', views.membership, name="membership"),
    path('gallery/', views.gallery, name="gallery"),
    path('news/', views.news, name="news"),
    path('events/delete/<int:event_id>/', views.delete_event, name='event_delete'),
    path('eventadd/', views.eventadd, name="eventadd"),
    path('add_image_template/', views.add_image_template, name="add_image_template"),
    path('gallery/delete/<int:id>', views.GalleryUploadDelete.as_view(), name='galleryimagedelete'),
    path('logout/', views.user_logout, name='logout'),
    path('user/details/<str:slug>', views.user_details_vew, name='individual_user_details'),
    path('user/admin/approve/<str:slug>', views.admin_approval, name='user_approval'),

    # latest URLs
    path('user/login', views.user_login_page, name='login_page'),
    path('user/registration/', views.user_registration, name='user_registration'),
    path('user/profile/details/', views.user_profile_details, name='user_profile_details')
]
