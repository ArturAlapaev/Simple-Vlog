import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    all_post = Post.objects.all()
    print(all_post)
    return HttpResponse(all_post[0].description)
