from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse

from .models import CustomerUserCreation


# Create your views here.
def dashboard(request):
    return render(request, "registration/dashboard.html")


def register(request):
    if request.method == 'GET':
        return render(request, "registration/registration.html", {"forms": CustomerUserCreation})
    elif request.method == 'POST':
        form = CustomerUserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
