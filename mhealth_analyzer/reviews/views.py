from django.shortcuts import render
# Go up one directory from 'reviews/' to the project root to find 'analysis_engine'
from analysis_engine.predictor import predictor_instance 

def index(request):
    context = {}
    if request.method == 'POST':
        review_text = request.POST.get('review_text', '')
        if review_text:
            # Call the prediction method from our global predictor instance
            predictions = predictor_instance.predict(review_text)
            context['results'] = predictions
            context['submitted_text'] = review_text
    
    return render(request, 'reviews/index.html', context)