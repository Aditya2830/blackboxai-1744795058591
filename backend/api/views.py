from rest_framework.decorators import api_view
from rest_framework.response import Response

def generate_mcqs(text):
    # Simple mock NLP function to generate MCQs from text
    # For demonstration, split text into sentences and create dummy questions
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    mcqs = []
    for i, sentence in enumerate(sentences[:5]):  # limit to 5 questions
        question = f"What is the meaning of: '{sentence[:50]}...?'"
        options = [
            sentence[:50],
            "Option 2",
            "Option 3",
            "Option 4"
        ]
        answer = sentence[:50]
        mcqs.append({
            'question': question,
            'options': options,
            'answer': answer
        })
    return mcqs

@api_view(['POST'])
def generate_quiz(request):
    data = request.data
    text = data.get('text', '')
    if not text:
        return Response({'error': 'No text provided'}, status=400)
    mcqs = generate_mcqs(text)
    return Response({'mcqs': mcqs})
