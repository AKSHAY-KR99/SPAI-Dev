from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from . import models, forms
from .models import GalleryManagement


# Create your views here.
def index(request):
    context = {'page': 'main'}
    return render(request, 'mainpages/home.html', context)

#About******************************************************************
def about(request):
    context = {'page': 'about'}
    return render(request, 'mainpages/about.html', context)

def exe_members(request):
    context = {'page': 'about','page2':'exe_members'}
    return render(request, 'about/exe_members.html', context)

def history(request):
    context = {'page': 'about','page2':'history'}
    return render(request, 'about/history.html', context)

def about_members(request):
    context = {'page': 'about','page2':'members'}
    return render(request, 'about/members.html', context)

def v_and_m(request):
    context = {'page': 'about','page2':'v_and_m'}
    return render(request, 'about/vision_and_mission.html', context)
#*****************************************************

#Members*************************************
def members(request):
    context = {'page': 'members'}
    return render(request, 'mainpages/members.html', context)

def membership(request):
    context = {'page': 'members','page2':'membership'}
    return render(request, 'members/membership.html', context)
#************************************************************

#publications************************************************
def publications(request):
    context = {'page': 'publications'}
    return render(request, 'mainpages/publications.html', context)

def editorial(request):
    context = {'page': 'publications','page2':'editorial'}
    return render(request, 'publications/editorial.html', context) 

def journal(request):
    context = {'page': 'publications','page2':'journal'}
    return render(request, 'publications/journal.html', context) 

def submit_paper(request):
    context = {'page': 'publications','page2':'submit_paper'}
    return render(request, 'publications/submit_paper.html', context) 

#****************************************************
def gallery(request):
    gallery_objects = GalleryManagement.objects.all()
    context = {'page': 'gallery','gallery_objects': gallery_objects}
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

def search(request):
    context = {'page': 'search'}
    return render(request, 'mainpages/search.html', context)


class Login(TemplateView):
    template_name = 'mainpages/login.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class GalleryManagementView(TemplateView):
    template_name = 'mainpages/gallery.html'
    model = models.GalleryManagement
    form_class = forms.GalleryManagementForm
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        pass
