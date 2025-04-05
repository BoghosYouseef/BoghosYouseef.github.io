from django.urls import path, include

from . import views

app_name = "codingBlog"

urlpatterns = [
    path("", views.home),
]
