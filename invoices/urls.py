from django.urls import path
from django.shortcuts import redirect
from .views import simple_upload, show_table, download_csv, download_xls


def redirect_to_home(request):
    return redirect("simple_upload")


urlpatterns = [
    path("", redirect_to_home, name="home"),
    path("simple_upload/", simple_upload, name="simple_upload"),
    path("table/", show_table, name="show_table"),
    path("download/csv/", download_csv, name="download_csv"),
    path("download/xls/", download_xls, name="download_xls"),
]
