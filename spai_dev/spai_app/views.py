import datetime
import os

import pdfkit
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.urls import reverse
from django.core.paginator import Paginator

from . import models, forms
from .models import GalleryManagement, User, EventManagement, UserDetailModel


# Create your views here.
def index(request):
    context = {}
    return render(request, 'mainpages/home.html', context)


def history(request):
    context = {'page': 'about', 'page2': 'history'}
    return render(request, 'mainpages/history.html', context)


@login_required
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


def members(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'mainpages/members.html', context)


def membership(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logout(request)
            return redirect("login")
        else:
            context = {'page': 'members', 'page2': 'membership', "form": form}
            return render(request, "members/membership.html", context)
    else:
        form = forms.UserRegistrationForm()
        context = {'page': 'members', 'page2': 'membership', "form": form}
        return render(request, "members/membership.html", context)


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
    event_object = EventManagement.objects.all().order_by('-id')
    paginator = Paginator(event_object, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    admin_key = True
    context = {'page_obj': page_obj, 'event_object': event_object, 'admin_key': admin_key}
    return render(request, 'mainpages/news.html', context)


def news_detail(request, pk):
    event_object = EventManagement.objects.get(pk=pk)
    context = {"event": event_object}
    return render(request, 'mainpages/news_details.html', context)


def eventadd(request):
    if request.POST:
        frm = forms.EventManagementForm(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            print("success")
            return redirect('news')
    else:
        frm = forms.EventManagementForm()
    context = {'page': 'news', 'frm': frm}
    return render(request, 'admin/eventadd.html', context)


def delete_event(request, event_id):
    event = get_object_or_404(EventManagement, id=event_id)
    event.delete()
    return redirect(reverse('news'))


def add_image_template(request):
    if request.POST:
        frm = forms.GalleryManagementForm(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            print("success")
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


class GalleryUploadDelete(TemplateView):
    template_name = 'mainpages/gallery.html'
    model = models.GalleryManagement
    form_class = forms.GalleryManagementForm
    context = {}

    def get(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs["id"])
        instance.delete()
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
        user_data = {}
        context = {}
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
        context['user'] = user_data

        return render(request, 'members/individual_user_details.html', context)
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


def certificate(request):
    if request.user.is_authenticated and request.user.admin_approved:
        user = User.objects.get(slug_value=request.user.slug_value)
        context = {"name": user.first_name, "email": user.email, "date":user.date_created,
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

