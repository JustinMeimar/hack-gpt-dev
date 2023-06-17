from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Painting

def image_gallery(request):
    images = Painting.objects.all()
    return render(request, 'api/gallery.html', {'images' : images})