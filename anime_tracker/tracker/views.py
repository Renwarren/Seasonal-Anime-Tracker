from django.shortcuts import render
from .kitsu_api import get_trending_anime

def my_view(request):
    data = get_trending_anime()
    return render(request, 'my_template.html', {'data': data})

# Create your views here.
