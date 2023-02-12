from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("login", views.Login.as_view(), name="login"),
    path("vehicle", views.VehicleList.as_view(), name="vehicle"),
    path("admin/", admin.site.urls),
]
