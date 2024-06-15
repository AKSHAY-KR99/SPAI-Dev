from django.shortcuts import render

# Create your views here.
def index(request):
    context={'page':'main'}
    return render(request,'main.html',context)

def about(request):
    context={'page':'about'}
    return render(request,'mainpages/about.html',context)

def members(request):
    context={'page':'members'}
    return render(request,'mainpages/members.html',context)

def gallery(request):
    context={'page':'gallery'}
    return render(request,'mainpages/gallery.html',context)

def accademics(request):
    context={'page':'accademics'}
    return render(request,'mainpages/accademics.html',context)

def news(request):
    context={'page':'news'}
    return render(request,'mainpages/news.html',context)

def publications(request):
    context={'page':'publications'}
    return render(request,'mainpages/publications.html',context)

def search(request):
    context={'page':'search'}
    return render(request,'mainpages/search.html',context)

