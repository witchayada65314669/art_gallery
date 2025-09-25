from django.shortcuts import render
from .models import Artwork

def index(request):
    artworks = Artwork.objects.all()
    return render(request, 'index.html', {'artworks': artworks})