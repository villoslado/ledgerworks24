from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SimpleUploadForm
from .utils import process_invoices
import pandas as pd
import os
import tempfile


@login_required
def simple_upload(request):
    if request.method == "POST":
        print("POST request received")
        print(f"request.POST: {request.POST}")
        print(f"request.FILES: {request.FILES}")

        # Manually handle files without form validation
        if "files" in request.FILES:
            files = request.FILES.getlist("files")
            temp_dir = tempfile.mkdtemp()
            file_paths = []

            for file in files:
                file_path = os.path.join(temp_dir, file.name)
                with open(file_path, "wb+") as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                file_paths.append(file_path)

            # Process the files
            df = process_invoices(file_paths)
            request.session["data"] = df.to_dict("records")

            return redirect("show_table")
        else:
            print("No files found in request.FILES")
            return HttpResponse("No files uploaded")
    else:
        form = SimpleUploadForm()
    return render(request, "invoices/simple_upload.html", {"form": form})


@login_required
def show_table(request):
    data = request.session.get("data")
    if data is None:
        return redirect("simple_upload")
    df = pd.DataFrame(data)
    return render(
        request,
        "invoices/table.html",
        {"data": df.to_html(index=False, classes="display")},
    )


@login_required
def download_csv(request):
    data = request.session.get("data")
    if data is None:
        return redirect("simple_upload")
    df = pd.DataFrame(data)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="invoices.csv"'
    df.to_csv(response, index=False)
    return response


@login_required
def download_xls(request):
    data = request.session.get("data")
    if data is None:
        return redirect("simple_upload")
    df = pd.DataFrame(data)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="invoices.xlsx"'
    df.to_excel(response, index=False, engine="openpyxl")
    return response
