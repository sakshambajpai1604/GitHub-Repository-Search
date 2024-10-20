import requests
from django.shortcuts import render

# Create your views here.
import requests

def search_repositories(request):
    query = request.GET.get('q', '')
    repositories = []

    if query:
        url = f'https://api.github.com/search/repositories?q={query}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            repositories = data.get('items', [])

    context = {
        'repositories': repositories,
        'query': query
    }
    return render(request, 'searchapp/search.html', context)
