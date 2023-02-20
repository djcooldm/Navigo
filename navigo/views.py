from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from navigo.models import Vehicle


class DashboardView(View):
    template = "navigo/index.html"
    login_url = "login"

    def get(self, request):
        return render(request, self.template)

class UserHomeView(View):
    template = "navigo/user_home.html"
    login_url = "login"

    def get(self, request):
        return render(request, self.template)


class Login(View):
    template = "navigo/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, self.template, {"form": form})

class VehicleView(View):
    template = "navigo/vehicle.html"
    login_url = "login"

    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, self.template, {'vehicles': vehicles})


class ListingView(View):
    template = "navigo/listing.html"
    login_url = "login"

    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, self.template, {'vehicles': vehicles})

