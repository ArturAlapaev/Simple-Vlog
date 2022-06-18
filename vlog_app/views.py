from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import datetime

# Create your views here.
def index(request):
    all_post = Post.objects.all()
    # return HttpResponse(f"{all_post[0].description}")
    context={
        "all_posts": all_post,
        "test": 123
    }
    return render(
        request=request,
        template_name='vlog_app/index.html',
        context=context
        )
    
def post_detail(requst):
    
    return render(
        request=requst,
        template_name="vlog_app/post-datail.html"
    )
