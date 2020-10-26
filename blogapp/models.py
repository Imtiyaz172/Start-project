from django.db import models
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe 
import os

# Create your models here.
class Logo(models.Model):
    Title       = models.CharField(max_length=50)
    Image       = models.ImageField(upload_to="logo/",blank= True)
    icon        = models.ImageField(upload_to="logo/",blank= True)
    Status      = models.BooleanField(default = True)
    header_image = models.ImageField(upload_to="logo/",blank= True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos' 