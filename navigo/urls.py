from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),
    path("home", views.UserHomeView.as_view(), name="home"),
    path("login", views.Login.as_view(), name="login"),
    path("vehicle", views.VehicleView.as_view(), name="vehicle"),
    path("listing", views.ListingView.as_view(), name="listing"),
    path("admin/", admin.site.urls),
]
