from django.urls import path
from .views import index, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('post-detail/', post_detail, name="post-detail")
]