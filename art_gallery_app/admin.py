# art_gallery_app/admin.py
from django.contrib import admin
from .models import Artwork

admin.site.register(Artwork)