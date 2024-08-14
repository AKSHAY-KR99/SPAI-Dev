from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('history/', views.history, name="history"),
    path('about_members/', views.about_members, name="about_members"),
    path('gallery/', views.gallery, name="gallery"),
    path('news/', views.news, name="news"),
    path('news/<int:pk>/', views.news_detail, name="news_detail"),
    path('events/delete/<int:event_id>/', views.delete_event, name='event_delete'),
    path('eventadd/', views.eventadd, name="eventadd"),
    path('add_image_template/', views.add_image_template, name="add_image_template"),

    # latest URLs
    path('user/login', views.user_login_page, name='login_page'),
    path('user/registration/', views.user_registration, name='user_registration'),
    path('user/profile/details/', views.user_profile_details, name='user_profile_details'),
    path('members/', views.members, name="members"),
    path('logout/', views.user_logout, name='logout'),
    path('user/detail/<str:slug>', views.user_details_vew, name='individual_user_details'),
    path('user/admin/approve/<str:slug>', views.admin_approval, name='user_approval'),
    path('user/admin/reject/<str:slug>', views.admin_rejection, name='user_reject'),
    path('certificate/<str:slug>', views.certificate, name='certificate'),
    path('gallery/delete/<int:id>', views.delete_gallery_item, name='galleryimagedelete')

]
