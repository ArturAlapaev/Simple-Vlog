from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, SITE_INFO
from .forms import CreatePostForm, EditPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.


def index(request):
    all_posts = Post.objects.filter(is_draft=False, is_delete=False)

    context = {
        "all_posts": all_posts,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    return render(
        request=request,
        template_name='vlog_app/index.html',
        context=context
    )


@login_required
def my_profile(request):
    all_posts = Post.objects.filter(user__id=request.user.id, is_delete=False)

    context = {
        "all_posts": all_posts,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    return render(
        request=request,
        template_name='vlog_app/my-profile.html',
        context=context
    )


def registration(request):

    form = UserCreationForm()

    context = {
        "form": form,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(
        request=request,
        template_name='registration/sign-up.html',
        context=context,
    )


@login_required
def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id, is_draft=False, is_delete=False)

    context = {
        "post": post,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    return render(
        request=request,
        template_name="vlog_app/post-detail.html",
        context=context
    )


@login_required
def create_post(request):

    form = CreatePostForm()

    context = {
        "form": form,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user_id=request.user.id)
            return redirect('my-profile')

    return render(
        request=request,
        template_name='vlog_app/post-create.html',
        context=context
    )


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        user__id=request.user.id,
        is_delete=False
    )
    form = EditPostForm(
        instance=post
    )

    context = {
        "form": form,
        "contacts": SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == "POST":

        form = EditPostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid:
            form.save()
            return redirect('/')

    return render(
        request=request,
        template_name='vlog_app/edit-post.html',
        context=context,
    )
