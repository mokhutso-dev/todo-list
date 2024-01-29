from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.viewId, name="view"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="index"),
    path("<int:id>", views.index, name="index"),
]