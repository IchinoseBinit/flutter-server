from django.shortcuts import render
from . import models
# Create your views here.

def load(request):
    obj = models.Apk.objects.first()
    print(obj.file)
    return render(request, 'home.html', {'file_path': obj.file})

