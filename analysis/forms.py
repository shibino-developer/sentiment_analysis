from django import forms

class TextForm(forms.Form):
    user_text = forms.CharField(widget=forms.Textarea, label='Enter text for sentiment analysis')
