from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from . import models, forms
from .models import GalleryManagement, User, EventManagement


# Create your views here.
def index(request):
    context = {'page': 'main'}
    return render(request, 'mainpages/home.html', context)


def about(request):
    context = {'page': 'about'}
    return render(request, 'mainpages/about.html', context)


def exe_members(request):
    context = {'page': 'about', 'page2': 'exe_members'}
    return render(request, 'about/exe_members.html', context)


def history(request):
    context = {'page': 'about', 'page2': 'history'}
    return render(request, 'about/history.html', context)


def about_members(request):
    context = {'page': 'about', 'page2': 'members'}
    return render(request, 'about/members.html', context)


def v_and_m(request):
    context = {'page': 'about', 'page2': 'v_and_m'}
    return render(request, 'about/vision_and_mission.html', context)


def members(request):
    context = {'page': 'members'}
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


def publications(request):
    context = {'page': 'publications'}
    return render(request, 'mainpages/publications.html', context)


def editorial(request):
    context = {'page': 'publications', 'page2': 'editorial'}
    return render(request, 'publications/editorial.html', context)


def journal(request):
    context = {'page': 'publications', 'page2': 'journal'}
    return render(request, 'publications/journal.html', context)


def submit_paper(request):
    context = {'page': 'publications', 'page2': 'submit_paper'}
    return render(request, 'publications/submit_paper.html', context)


def gallery(request):
    admin_key = False
    if request.user.is_superuser:
        admin_key = True
    gallery_objects = GalleryManagement.objects.all()
    context = {'page': 'gallery', 'gallery_objects': gallery_objects, 'admin_key': admin_key}
    return render(request, 'mainpages/gallery.html', context)


def accademics(request):
    context = {'page': 'accademics'}
    return render(request, 'mainpages/accademics.html', context)


def news(request):
    event_object = EventManagement.objects.all()
    context = {'page': 'news', 'event_object': event_object}
    return render(request, 'mainpages/news.html', context)


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


def search(request):
    context = {'page': 'search'}
    return render(request, 'mainpages/search.html', context)


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
def user_detail_upload(request):
    if request.method == 'POST':
        form = forms.UserDetailForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_status_change(request.user.slug_value, request.user.status)
            return redirect('index')  # redirect to a success page
    else:
        form = forms.UserDetailForm(request.user)
    return render(request, 'user_detail_add.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('gallery')


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
