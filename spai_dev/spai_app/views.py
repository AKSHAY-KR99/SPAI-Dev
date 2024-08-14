from django.utils import timezone
import datetime
import os

import pdfkit

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.urls import reverse
from django.core.paginator import Paginator

from . import models, forms
from .models import GalleryManagement, User, EventManagement, UserDetailModel


def index(request):
    now = timezone.now()
    upcoming_events = list(EventManagement.objects.filter(datetime__gte=now).order_by('datetime')[:3])
    if len(upcoming_events) < 3:
        remaining_slots = 3 - len(upcoming_events)
        past_events = list(EventManagement.objects.filter(datetime__lt=now).order_by('-datetime')[:remaining_slots])
        upcoming_events.extend(past_events)
    context = {
        'upcoming_events': upcoming_events,
    }
    return render(request, 'mainpages/home.html', context)
    # return render(request, 'members/members.html', context)
    # return render(request, 'members/payment_page.html', context)


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


@login_required
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
    context = {
        "event": event_object,
        'related_events': upcoming_events,
    }
    return render(request, 'mainpages/news_details.html', context)


@login_required
def eventadd(request):
    if request.method == 'POST' and request.user.user_role == settings.ADMIN_ROLE_VALUE:
        title = request.POST['title']
        image = request.FILES['image']
        datetime = request.POST['datetime']
        location = request.POST['location']
        description = request.POST.get('description', '')
        registration_link = request.POST.get('registration_link', '')

        EventManagement.objects.create(
            title=title,
            image=image,
            datetime=datetime,
            location=location,
            description=description,
            registration_link=registration_link
        )
        return redirect('news')  # Redirect to a success page after creation

    return render(request, 'admin/eventadd.html')


@login_required
def delete_event(request, event_id):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        event = get_object_or_404(EventManagement, id=event_id)
        event.delete()
        return redirect(reverse('news'))
    return redirect(reverse('news'))


@login_required
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


@login_required
def delete_gallery_item(request, *args, **kwargs):
    if request.user.user_role == settings.ADMIN_ROLE_VALUE:
        try:
            instance = models.GalleryManagement.objects.get(id=kwargs["id"])
            instance.delete()
            return redirect("gallery")
        except:
            return redirect("gallery")
    return redirect("gallery")


@login_required
def user_profile_details(request):
    if request.method == 'POST':
        form = forms.UserDetailForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_status_change(request.user.slug_value, request.user.status)
            return redirect('index')  # redirect to a success page
    else:
        form = forms.UserDetailForm(request.user)
    return render(request, 'members/user_profile_details.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def user_details_vew(request, *args, **kwargs):
    slug = kwargs.get("slug", None)
    if request.user.user_role == settings.ADMIN_ROLE_VALUE or request.user.slug_value == slug:
        context = {}
        user_data = get_user_full_details(slug)
        context['user'] = user_data
        return render(request, 'members/member_details.html', context)
    else:
        return redirect('login')


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


def user_status_change(slug, current_status):
    user = User.objects.get(slug_value=slug)
    if user is not None:
        if current_status == settings.USER_CREATED:
            user.status = settings.USER_DETAILS_ADDED
        elif current_status == settings.USER_DETAILS_ADDED:
            user.status = settings.ADMIN_APPROVAL_PENDING
        elif current_status == settings.ADMIN_APPROVAL_PENDING:
            user.status = settings.ADMIN_APPROVED
        else:
            pass
        user.save()


def get_next_step(status):
    if status == settings.USER_CREATED:
        return 'User details adding pending'
    if status == settings.USER_DETAILS_ADDED:
        return 'Admin approval pending'
    if status == settings.ADMIN_APPROVAL_PENDING:
        return 'Admin Approved, No action needed'
    if status == settings.ADMIN_REJECTED:
        return 'Admin Rejected'


def certificate(request, *args, **kwargs):
    slug = kwargs.get("slug", None)
    if request.user.is_authenticated and request.user.admin_approved:
        if request.user.user_role == settings.ADMIN_ROLE_VALUE:
            user = User.objects.get(slug_value=slug)
        else:
            user = User.objects.get(slug_value=request.user.slug_value)
        context = {"name": user.first_name, "email": user.email, "date": user.date_created,
                   "current_date": datetime.date.today(), "current_time": datetime.datetime.now().time()}
        wkhtml_to_pdf = os.path.join(settings.BASE_DIR, "wkhtmltopdf.exe")
        template_path = 'pdf_template.html'
        template = get_template(template_path)
        html = template.render(context)
        config = pdfkit.configuration(wkhtmltopdf=wkhtml_to_pdf)
        pdf = pdfkit.from_string(html, False, configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{user.first_name}_certificate.pdf"'
        return response
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
    return user_data


def admin_action(status):
    if status == settings.USER_DETAILS_ADDED:
        return 'Admin approval pending'
    return 'No action needed'


# certificate download
# status change for admin and other user
#
# payment model
#
# login authentication error
