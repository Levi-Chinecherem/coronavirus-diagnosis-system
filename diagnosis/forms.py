# from django import forms
# from .symptoms import SYMPTOMS

# class DiagnosisReportForm(forms.Form):
#     selected_symptoms = forms.MultipleChoiceField(
#         choices=[(symptom["name"], symptom["name"]) for symptom in SYMPTOMS],
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
#         label="Select your symptoms:",
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         label="Please describe your condition:",
#     )

from django import forms
from .models import Symptom

class DiagnosisReportForm(forms.Form):
    selected_symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label="Select your symptoms:",
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label="Please describe your condition:",
    )
