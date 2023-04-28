from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse("Here are our projects")


def project(request):
    return HttpResponse("Single Project")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", projects, name="projects")
]
