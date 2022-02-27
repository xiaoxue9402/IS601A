from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://random.dog/woof.json?ref=apilist.fun')
    data = response.json()
    image = data['url']
    print(image)
    return render(request, 'index.html', {
        'url':image
    })

# Create your views here.
