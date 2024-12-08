import datetime

from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse
from django.core.paginator import Paginator

from . import models, forms
from .models import GalleryManagement, User, EventManagement, UserDetailModel, GalleryImage, PaymentModel
from .decorators import admin_only, authenticated_only
from .utils import render_to_pdf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import LifeMembers
from .serializers import LifeMembersSerializer


# Frequently used methods
def admin_action(sts):
    if sts == settings.USER_DETAILS_ADDED:
        return 'Admin approval pending'
    return 'No action needed'


def user_status_change(slug, current_status):
    user = User.objects.get(slug_value=slug)
    if user is not None:
        if current_status == settings.USER_CREATED:
            user.status = settings.USER_DETAILS_ADDED
        elif current_status == settings.USER_DETAILS_ADDED:
            user.status = settings.PAYMENT_PENDING
        elif current_status == settings.PAYMENT_PENDING:
            user.status = settings.PAYMENT_DONE
        elif current_status == settings.PAYMENT_DONE:
            user.status = settings.ADMIN_APPROVAL_PENDING
        elif current_status == settings.ADMIN_APPROVAL_PENDING:
            user.status = settings.ADMIN_APPROVED
        else:
            pass
        user.save()


def get_next_step(status):
    if status == settings.USER_CREATED:
        return 'User created, Details not added'
    if status == settings.USER_DETAILS_ADDED:
        return 'User Details added, Payment not completed'
    if status == settings.PAYMENT_PENDING:
        return 'Payment Pending'
    if status == settings.PAYMENT_DONE:
        return 'Payment completed, Admin Approval Pending'
    if status in [settings.ADMIN_APPROVAL_PENDING, settings.ADMIN_APPROVED]:
        return 'Admin Approved, No action needed'
    if status == settings.ADMIN_REJECTED:
        return 'Admin Rejected'


# Views
def index(request):
    now = timezone.now()
    upcoming_events = list(EventManagement.objects.filter(datetime__gte=now).order_by('datetime')[:5])
    if len(upcoming_events) < 5:
        remaining_slots = 5 - len(upcoming_events)
        past_events = list(EventManagement.objects.filter(datetime__lt=now).order_by('-datetime')[:remaining_slots])
        upcoming_events.extend(past_events)
    context = {
        'upcoming_events': upcoming_events,
    }
    return render(request, 'mainpages/new_home.html', context)
    # return render(request, 'static_pages/about/about.html', context)
    # return render(request, 'members/payment_page.html', context)


def about_page(request):
    page = request.GET.get('page')
    if page == "about_spai":
        return render(request, 'static_pages/about/about.html')
    if page == "mission":
        return render(request, 'static_pages/about/mission.html')
    if page == "history":
        return render(request, 'static_pages/about/history.html')
    if page == "message_from_president":
        return render(request, 'static_pages/about/msgpresident.html')
    if page == "message_from_secretary":
        return render(request, 'static_pages/about/msgsecretary.html')
    if page == "president":
        return render(request, 'static_pages/about/leadership/president.html')
    if page == "secretary":
        return render(request, 'static_pages/about/leadership/secretary.html')
    if page == "patron":
        return render(request, 'static_pages/about/leadership/patron.html')
    if page == "committee":
        return render(request, 'static_pages/about/leadership/committee.html')
    if page == "pre_committee":
        return render(request, 'static_pages/about/leadership/previous_year.html')
    if page == "regional":
        return render(request, 'static_pages/about/leadership/regional.html')
    
def membership(request):
    page = request.GET.get('page')
    print(page)
    if page == "previlege":
        return render(request, 'static_pages/membership/previlege.html')
    if page == "major":
        return render(request, 'static_pages/news/major.html') 

def publications(request):
    page = request.GET.get('page')
    print(page)
    if page == "about_spai_journal":
        return render(request, 'static_pages/publications/spai_journel.html')
    if page == "editorial":
        return render(request, 'static_pages/publications/editorial.html')
    if page == "joinaseditor":
        return render(request, 'static_pages/publications/joinaseditor.html')
    if page == "joinasreviewer":
        return render(request, 'static_pages/publications/joinasreviewer.html')
    if page == "call_for_manuscripts":
        return render(request, 'static_pages/publications/call.html')
    if page == "journal_archives":
        return render(request, 'static_pages/publications/journalarchieve.html')  


def academic(request):
    page = request.GET.get('page')
    if page == "about_internship":
        return render(request, 'static_pages/academic/internship/about.html')
    if page == "upcoming_annual":
        return render(request, 'static_pages/academic/anual_conference/upcoming.html')
    if page == "past_annual":
        return render(request, 'static_pages/academic/anual_conference/past.html')
    if page == "annual_archives":
        return render(request, 'static_pages/academic/anual_conference/archives.html')
    if page == "spai_award":
        return render(request, 'static_pages/academic/awards/awards.html')
    if page == "paper_presenter":
        return render(request, 'static_pages/academic/awards/papper.html')
    if page == "poster_presentation":
        return render(request, 'static_pages/academic/awards/poster.html')
    if page == "publication":
        return render(request, 'static_pages/academic/awards/publications.html')
    if page == "research":
        return render(request, 'static_pages/academic/awards/research.html')
    if page == "student_research":
        return render(request, 'static_pages/academic/awards/student.html')
    if page == "research_grant":
        return render(request, 'static_pages/academic/grant/research.html')
    if page == "call_for_grants":
        return render(request, 'static_pages/academic/grant/call.html')
    if page == "mentors":
        return render(request, 'static_pages/academic/internship/mentors.html')
    if page == "internship_testimonials":
        return render(request, 'static_pages/academic/internship/testimonials.html')
    if page == "upcoming_online_webinars":
        return render(request, 'static_pages/academic/online/upcoming.html')
    if page == "completed_online_webinars":
        return render(request, 'static_pages/academic/online/past.html')
    if page == "upcoming_state_workshop":
        return render(request, 'static_pages/academic/state_workshop/upcomming.html')
    if page == "completed_state_workshop":
        return render(request, 'static_pages/academic/state_workshop/past.html')
    if page == "upcoming_national_workshop":
        return render(request, 'static_pages/academic/workshop/upcoming.html')
    if page == "completed_national_workshop":
        return render(request, 'static_pages/academic/workshop/past.html')
    if page == "certification":
        return render(request, 'static_pages/academic/certification.html')
    if page == "latest_update":
        return render(request, 'static_pages/academic/latest_update.html')
    if page == "mou":
        return render(request, 'static_pages/academic/mou.html')
    


def history(request):
    context = {'page': 'about', 'page2': 'history'}
    return render(request, 'mainpages/history.html', context)


def about_members(request):
    context = {}
    user_details_vew(request)
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        users = User.objects.all()
        for user in users:
            user.next_step = get_next_step(user.status)
        context['users'] = users
    context['page'] = 'about'
    context['page2'] = 'members'
    context['request'] = request
    return render(request, 'about/members.html', context)


@admin_only
def members(request):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        users = User.objects.all()
        user_list = []
        for user in users:
            user_data = get_user_full_details(user.slug_value)
            user_list.append(user_data)
        context = {'users': user_list}
        return render(request, 'members/members.html', context)


def user_registration(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logout(request)
            return redirect("login_page")
        else:
            context = {"form": form}
            return render(request, "members/user_registration.html", context)
    else:
        form = forms.UserRegistrationForm()
        context = {"form": form}
        return render(request, "members/user_registration.html", context)


def gallery(request):
    gallery_objects = GalleryManagement.objects.all()
    context = {'page': 'gallery', 'gallery_objects': gallery_objects}
    return render(request, 'mainpages/gallery.html', context)


def gallery_list(request):
    galleries = GalleryManagement.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(galleries, 9)
    page_obj = paginator.get_page(page_number)
    context = {'galleries': galleries, 'page_obj': page_obj}
    return render(request, 'mainpages/gallery.html', context)


def gallery_detail(request, pk):
    gallery = GalleryManagement.objects.get(pk=pk)
    images = GalleryImage.objects.filter(gallery=gallery)
    return render(request, 'mainpages/gallery_detail.html', {'gallery': gallery, 'images': images})


def gallery_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        place = request.POST.get('place')
        image = request.FILES.get('mainimage')
        gallery = GalleryManagement.objects.create(
            image_name=title,
            description=description,
            place=place,
            image=image
        )

        # Loop through the files in request.FILES
        for key in request.FILES:
            image = request.FILES[key]
            GalleryImage.objects.create(gallery=gallery, images=image)

        return redirect('gallery_list')  # Return a success response

    return render(request, 'admin/galleryadd.html')  # Render the add gallery template


@admin_only
def gallery_delete(request, pk):
    gallery = get_object_or_404(GalleryManagement, pk=pk)
    gallery.delete()
    return redirect('gallery_list')


def delete_gallery_image(request, image_id):
    # Get the image object or return a 404 if not found
    obj = GalleryImage.objects.get(pk=image_id)
    gallery_id = obj.gallery.pk  # Save gallery ID to redirect back later

    # Delete the image file
    obj.delete()

    # Add a success message
    messages.success(request, 'Image deleted successfully.')

    # Redirect back to the gallery detail page
    return redirect('gallery_detail', pk=gallery_id)


def add_gallery_image(request, gallery_id):
    gallery = get_object_or_404(GalleryManagement, id=gallery_id)

    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        # Create a new GalleryImage object
        new_image = GalleryImage.objects.create(gallery=gallery, images=image)
        new_image.save()
        messages.success(request, 'Image added successfully.')
        return redirect('gallery_detail', pk=gallery_id)

    return redirect('gallery_detail', pk=gallery_id)


def news(request):
    all_events = EventManagement.objects.all().order_by('-id')
    upcoming_events = EventManagement.objects.filter(datetime__gte=timezone.now()).order_by('datetime')
    past_events = EventManagement.objects.filter(datetime__lt=timezone.now()).order_by('-datetime')

    page_number = request.GET.get('page', 1)
    current_tab = request.GET.get('tab', 'all')

    if current_tab == 'upcoming':
        paginator = Paginator(upcoming_events, 9)
    elif current_tab == 'post':
        paginator = Paginator(past_events, 9)
    else:
        paginator = Paginator(all_events, 9)
        current_tab = 'all'  # Default to 'all' if the tab is not specified
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'current_tab': current_tab,
    }
    return render(request, 'mainpages/news.html', context)


def news_detail(request, pk):
    event_object = EventManagement.objects.get(pk=pk)
    upcoming_events = list(EventManagement.objects.filter(datetime__gt=event_object.datetime).order_by('datetime')[:3])
    if len(upcoming_events) < 3:
        remaining_slots = 3 - len(upcoming_events)
        past_events = list(
            EventManagement.objects.filter(datetime__lt=event_object.datetime).order_by('-datetime')[:remaining_slots])
        upcoming_events.extend(past_events)
    if GalleryManagement.objects.filter(event=event_object).exists():
        gallery = GalleryManagement.objects.get(event=event_object)
    else:
        gallery = None
    context = {
        "event": event_object,
        'related_events': upcoming_events,
        "gallery": gallery
    }
    return render(request, 'mainpages/news_details.html', context)


def eventadd(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        datetime = request.POST['datetime']
        location = request.POST['location']
        description = request.POST.get('description', '')
        registration_link = request.POST.get('registration_link', '')

        event = EventManagement.objects.create(
            title=title,
            image=image,
            datetime=datetime,
            location=location,
            description=description,
            registration_link=registration_link
        )
        # Check if the checkbox for multiple images is checked
        if 'multipleImagesCheck' in request.POST:
            gallery = GalleryManagement.objects.create(
                image=image,
                upload_date=datetime,
                image_name=title,
                description=description,
                event=event,
                place=location
            )

            # Handle multiple images upload
            multiple_images = request.FILES.getlist('multiple_images')
            GalleryImage.objects.create(gallery=gallery, images=image)
            for image_file in multiple_images:
                GalleryImage.objects.create(gallery=gallery, images=image_file)
        return redirect('news')  # Redirect to a success page after creation

    return render(request, 'admin/eventadd.html')


@admin_only
def delete_event(request, event_id):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        event = get_object_or_404(EventManagement, id=event_id)
        event.delete()
        return redirect(reverse('news'))
    return redirect(reverse('news'))


@admin_only
def add_image_template(request):
    if request.POST and request.user.user_role == settings.ADMIN_ROLE_VALUE:
        frm = forms.GalleryManagementForm(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            return redirect('gallery')
    else:
        frm = forms.GalleryManagementForm()
    context = {'page': 'gallery', 'frm': frm}
    return render(request, 'admin/add_image_template.html', context)


def user_login(request):
    form = forms.UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if request.user.status == settings.USER_CREATED:
                return redirect('user_detail')
            else:
                return redirect('index')
    return render(request, 'mainpages/login.html', {'form': form})


@admin_only
def delete_gallery_item(request, *args, **kwargs):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        try:
            instance = models.GalleryManagement.objects.get(id=kwargs["id"])
            instance.delete()
            return redirect("gallery")
        except:
            return redirect("gallery")
    return redirect("gallery")


@authenticated_only
def user_profile_details(request):
    if request.method == 'POST':
        form = forms.UserDetailForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            request.user.status = settings.USER_DETAILS_ADDED
            request.user.save()
            form.save()
            user_status_change(request.user.slug_value, request.user.status)
            return redirect('payment_model', slug=request.user.slug_value)  # redirect to a success page
    else:
        form = forms.UserDetailForm(request.user)
    return render(request, 'members/user_profile_details.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


@authenticated_only
def user_details_vew(request, *args, **kwargs):
    slug = kwargs.get("slug", None)
    if request.user.user_role == settings.ADMIN_ROLE_VALUE or request.user.slug_value == slug:
        context = {}
        user_data = get_user_full_details(slug)
        context['user'] = user_data
        return render(request, 'members/member_details.html', context)
    else:
        return redirect('login')


@admin_only
def admin_approval(request, *args, **kwargs):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        slug = kwargs.get("slug", None)
        user = User.objects.filter(slug_value=slug).first()
        if user is None:
            return redirect("members")
        user.admin_approved = True
        user.save()
        user_status_change(slug, user.status)
        return redirect('members')
    else:
        return redirect('login_page')


@admin_only
def admin_rejection(request, *args, **kwargs):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        slug = kwargs.get("slug", None)
        user = User.objects.filter(slug_value=slug).first()
        if user is None:
            return redirect("members")
        user.admin_approved = False
        user.status = settings.ADMIN_REJECTED
        user.save()
        return redirect('members')
    else:
        return redirect('login_page')


def user_login_page(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if request.user.status == settings.USER_CREATED:
                    return redirect('user_profile_details')
                else:
                    return redirect('index')
    else:
        form = forms.UserLoginForm()
    return render(request, 'members/user_login.html', {'form': form})


@authenticated_only
def certificate(request, *args, **kwargs):
    slug = kwargs.get("slug", None)
    if request.user.is_authenticated and request.user.admin_approved:
        if request.user.user_role == settings.ADMIN_ROLE_VALUE:
            user = User.objects.get(slug_value=slug)
        else:
            user = User.objects.get(slug_value=request.user.slug_value)
        context = {"name": user.first_name, "email": user.email, "date": user.date_created}
        template_path = 'pdf_template.html'
        template = get_template(template_path)
        html = template.render(context)
        pdf = render_to_pdf(template_path, context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"{user.username}_certificate.pdf"
            content = f"inline; filename={filename}"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Something went wrong..!")
    else:
        return redirect('login_page')


def get_user_full_details(slug):
    user_data = {}
    user = User.objects.filter(slug_value=slug).first()
    if user is None:
        return redirect("about_members")
    user_dict = model_to_dict(user)
    user_data['email'] = user_dict.get("email", None)
    user_data['username'] = user_dict.get("username", None)
    user_data['first_name'] = user_dict.get("first_name", None)
    user_data['last_name'] = user_dict.get("last_name", None)
    user_data['state'] = user_dict.get("state", None)
    user_data['status'] = user_dict.get("status", None)
    user_data['slug_value'] = user_dict.get("slug_value", None)
    user_data['admin_approved'] = user_dict.get("admin_approved", None)
    user_data['next_step'] = get_next_step(user_dict.get("status", None))
    user_data['date_created'] = user.date_created
    user_data['admin_action'] = admin_action(user_dict.get("status", None))

    user_details = UserDetailModel.objects.filter(user=user.id).first()
    if user_details is not None:
        user_detail_dict = model_to_dict(user_details)
        user_data['degree'] = user_detail_dict.get("degree", None)
        user_data['profession'] = user_detail_dict.get("profession", None)
        user_data['institution'] = user_detail_dict.get("institution", None)
        user_data['department'] = user_detail_dict.get("department", None)
        user_data['address'] = user_detail_dict.get("address", None)
        user_data['phone_number'] = user_detail_dict.get("phone_number", None)
        user_data['alternate_number'] = user_detail_dict.get("alternate_number", None)
        user_data['alternate_mail'] = user_detail_dict.get("alternate_mail", None)
        user_data['photo'] = user_detail_dict.get("photo", None)
        user_data['specialized_in'] = user_detail_dict.get("specialized_in", None)
        user_data['research_interest'] = user_detail_dict.get("research_interest", None)
        user_data['payment'] = False

    payment_data = PaymentModel.objects.filter(user_info=user).order_by('-payment_reported_date').first()
    if payment_data is not None:
        payment_dict = model_to_dict(payment_data)
        user_data['payment'] = True
        user_data["transaction_id"] = payment_dict.get("transaction_id", None)
        user_data["reference_id"] = payment_dict.get("reference_id", None)
        user_data["bank_name"] = payment_dict.get("bank_name", None)
        p_t = payment_dict.get("payment_type", None)
        user_data["payment_type"] = settings.QR_CODE_NAME
        if p_t == settings.BANK_TRANSFER:
            user_data["payment_type"] = settings.BANK_TRANSFER_NAME
        user_data["payment_doc"] = payment_dict.get("document", None)
        user_data["payment_date"] = payment_data.payment_reported_date
    return user_data


@authenticated_only
def payment_model(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == 'POST':
            slug = kwargs.get("slug", None)
            user = User.objects.filter(slug_value=slug).first()
            if not user:
                return redirect("login_page")
            form = forms.PaymentForm(request.user, request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user_status_change(request.user.slug_value, request.user.status)
                return redirect("index")
        else:
            form = forms.PaymentForm(request.user)
        return render(request, 'members/payment_page.html', {'form': form})


def unauthorized_page_403(request):
    return render(request, 'permission/403_page.html')


# rest API
@api_view(['POST'])
def create_or_update_life_member(request):
    data = {key: (value if value != "" else None) for key, value in request.data.items()}

    name = data.get('name')
    life_member = None

    if name:
        life_member = LifeMembers.objects.filter(name=name).first()

    if life_member:
        serializer = LifeMembersSerializer(life_member, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(update_date=timezone.now())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = LifeMembersSerializer(data=data)
        if serializer.is_valid():
            serializer.save(upload_date=timezone.now(), update_date=timezone.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @admin_only
def life_members_get(request):
    members = LifeMembers.objects.all()
    context = {'members': members}
    return render(request, 'members/life_members.html', context)


# @admin_only
def life_member_info(request, *args, **kwargs):
    uid = kwargs.get("uid", None)
    context = {}
    user_data = LifeMembers.objects.get(uid=uid)
    context['user'] = user_data
    return render(request, 'members/life_member_details.html', context)


def internship_page(request):
    if request.method == 'POST':
        form = forms.InternshipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.InternshipApplicationForm()
    return render(request, 'internship/internship.html', {'form': form})


def list_applications(request):
    context = {}
    applications = models.InternshipApplication.objects.all()
    context['applications'] = applications
    return render(request, 'internship/list_applications.html', context)


@admin_only
def application_retrieve(request, *args, **kwargs):
    pk = kwargs.get("pk", None)
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        context = {}
        user_data = models.InternshipApplication.objects.get(pk=pk)
        context['user'] = user_data
        return render(request, 'internship/view_applications.html', context)
    else:
        return redirect('login')


def call_for_manuscript(request):
    context = {}
    return render(request, 'static_pages/publications/manuscript.html', context)
