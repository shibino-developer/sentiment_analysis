
from django.shortcuts import render
from .forms import TextForm
from analysis.sentiment import analyze_sentiment

def home(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            sentiment_scores = analyze_sentiment(text)
            return render(request, 'index.html', {
                'form': form,
                'sentiment_scores': sentiment_scores
            })
    else:
        form = TextForm()

    return render(request, 'index.html', {'form': form})