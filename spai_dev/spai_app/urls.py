from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('history/', views.history, name="history"),
    path('about_members/', views.about_members, name="about_members"),
    path('gallery/', views.gallery_list, name="gallery_list"),

    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    # path('gallery/<int:pk>/update/', views.gallery_update, name='gallery_update'),
    path('gallery/delete/<int:pk>/', views.gallery_delete, name='gallery_delete'),
    path('gallery/image/delete/<int:image_id>/', views.delete_gallery_image, name='delete_gallery_image'),
    path('gallery/image/add/<int:gallery_id>/', views.add_gallery_image, name='add_gallery_image'),

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
    path('get/life-members', views.life_members_get, name='life_members_get'),
    path('get/life-member/<str:uid>', views.life_member_info, name='life_member_info'),
    path('join-internship/', views.internship_page, name='internship_page'),
    path('list/applications/', views.list_applications, name='list_applications'),
    path('get/<int:pk>/application', views.application_retrieve, name='application_retrieve'),

    path('user/payment/<str:slug>', views.payment_model, name='payment_model'),

    # error pages
    path('unauthorized/403/', views.unauthorized_page_403, name='unauthorized_403'),

    path('about', views.about_page, name='about_page'),
    path('membership', views.membership, name='membership'),
    path('publications', views.publications, name='publications'),
    path('academic', views.academic, name='academic'),

    # rest api
    path('life-members', views.create_or_update_life_member, name='life-members')

]
