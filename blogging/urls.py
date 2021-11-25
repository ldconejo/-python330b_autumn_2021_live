from django.conf.urls import url
from django.urls import path
from blogging.views import stub_view
from blogging.views import list_view, detail_view

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
]
