from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="livestock-index"),
    path("about/", views.about, name="livestock-about"),
    path("cows/", views.cows, name="livestock-cows"),
    path("cows/<int:id>/", views.cow, name="livestock-cow"),
    path("api/cows", views.list_cows, name="livestock-api-cow")

]