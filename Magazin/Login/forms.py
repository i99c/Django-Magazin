from django import forms
from .models import Reader

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['user', 'phone', 'is_darkmode']
