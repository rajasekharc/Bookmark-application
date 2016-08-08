from django.shortcuts import render
from bookmark.forms import Bookmarkform
from .models import Website
from django.db.models import Q


def input(request):
    if request.method == "POST":
        form = Bookmarkform(request.POST)
        form.save()

    else:
        form = Bookmarkform()
    return render(request, 'index.html', {'form': form})


def list_website(request):
    web_add=Website.objects.all()
    return render(request,'display.html',{'web_add':web_add})


def search(request,key):
    web_add = Website.objects.filter(Q(website_address__icontains = key) | Q(description__icontains =key))
    return render(request, 'display.html', {'web_add': web_add})