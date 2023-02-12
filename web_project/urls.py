from django.urls import include, path

from navigo import views

urlpatterns = [
    path("navigo/", include("navigo.urls")),
]
