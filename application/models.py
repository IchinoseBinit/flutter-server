from django.db import models

# Create your models here.

class Apk(models.Model):
    file = models.FileField(upload_to="media", )
    upload_time = models.DateTimeField(auto_now_add=True,)


