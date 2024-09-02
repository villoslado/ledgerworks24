from django import forms
from .widgets import MultipleFileInput


class UploadFileForm(forms.Form):
    files = forms.FileField(widget=MultipleFileInput())


class SimpleUploadForm(forms.Form):
    # You can add other form fields here if needed
    pass
