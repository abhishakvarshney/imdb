from django import forms


class UploadJSONFileForm(forms.Form):
    file = forms.FileField()

