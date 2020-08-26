from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.information, name="info"),
    path("result", views.searchbar, name="search"),
    path("newpost", views.newpost, name="newpost"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.getrandom, name="random")
]
