# sentiment_analysis_tool/forms.py

from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Enter Text')
