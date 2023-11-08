from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = 'API KEY'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt = message,
        max_tokens =150,
        n=1,
        stop=None,
        # temparature=0.7,
    )

    answer =response.choices[0].text.strip()
    return answer

    

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html')