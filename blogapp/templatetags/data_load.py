from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from blogapp import models
register = template.Library()

@register.filter(name='logoreg')
def logoicon(request):
    logo  = models.Logo.objects.filter(Status = True).order_by("-id")
    return logo
