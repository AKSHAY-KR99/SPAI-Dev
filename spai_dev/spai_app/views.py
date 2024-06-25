from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from . import models, forms
from .models import GalleryManagement


# Create your views here.
def index(request):
    context = {'page': 'main'}
    return render(request, 'mainpages/home.html', context)


def about(request):
    context = {'page': 'about'}
    return render(request, 'mainpages/about.html', context)


def members(request):
    context = {'page': 'members'}
    return render(request, 'mainpages/members.html', context)


def gallery(request):
    admin_key = True
    gallery_objects = GalleryManagement.objects.all()
    context = {'page': 'gallery','gallery_objects': gallery_objects, 'admin_key': admin_key}
    return render(request, 'mainpages/gallery.html', context)


def accademics(request):
    context = {'page': 'accademics'}
    return render(request, 'mainpages/accademics.html', context)


def news(request):
    context = {'page': 'news'}
    return render(request, 'mainpages/news.html', context)


def add_image_template(request):
    if request.POST:
        frm=forms.GalleryManagementForm(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
            print("success")
            return redirect('gallery')
    else:
        frm=forms.GalleryManagementForm()
    context = {'page': 'gallery','frm':frm}
    return render(request, 'admin/add_image_template.html', context)

def publications(request):
    context = {'page': 'publications'}
    return render(request, 'mainpages/publications.html', context)


def search(request):
    context = {'page': 'search'}
    return render(request, 'mainpages/search.html', context)


class Login(TemplateView):
    template_name = 'mainpages/login.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class GalleryUploadDelete(TemplateView):
    template_name = 'mainpages/gallery.html'
    model = models.GalleryManagement
    form_class = forms.GalleryManagementForm
    context = {}

    def get(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs["id"])
        instance.delete()
        return redirect("gallery")
