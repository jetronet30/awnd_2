from django import forms

from .models import ResAiModel

class ResAiForm(forms.ModelForm):
    class Meta:
        model = ResAiModel
        fields = '__all__'