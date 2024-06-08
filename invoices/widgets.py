from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs["multiple"] = "multiple"
        return super().render(name, value, attrs, renderer)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, "getlist"):
            return files.getlist(name)
        else:
            return [files.get(name)]
