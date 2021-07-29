from django.shortcuts import render
from . import models
# Create your views here.

def load(request):
    obj = models.Apk.objects.first()
    file_path = None
    if obj is not None:
        file_path = obj.file
    return render(request, 'home.html', {'file_path': file_path})

