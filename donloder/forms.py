from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter video url', 'class':'input input-bordered input-accent w-full max-w-xs' }), label=False)
