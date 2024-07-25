import io
import base64
from django.shortcuts import render
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')

        # Initialize SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)

        # Generate the plot
        fig, ax = plt.subplots()
        labels = ['Positive', 'Neutral', 'Negative']
        scores = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']]
        ax.bar(labels, scores, color=['#28a745', '#6c757d', '#dc3545'])
        ax.set_ylabel('Score')
        ax.set_title('Sentiment Scores')

        # Save the plot to a BytesIO object and encode it
        buf = io.BytesIO()
        FigureCanvas(fig).print_png(buf)
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        return render(request, 'result.html', {
            'text': text,
            'sentiment_scores': sentiment_scores,
            'plot_url': image_base64
        })
    return render(request, 'index.html')
