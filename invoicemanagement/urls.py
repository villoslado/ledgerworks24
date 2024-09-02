from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_home(request):
    return redirect("simple_upload")


urlpatterns = [
    path("", redirect_to_home, name="home_page"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("invoices/", include("invoices.urls")),
]
