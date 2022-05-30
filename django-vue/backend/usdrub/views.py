# backend/notes/views.py
from rest_framework import viewsets

from .models import usdru
from .serializers import usdruSerializer

import requests

def home(request):
    response = requests.get('https://v6.exchangerate-api.com/v6/632cda93e818793dd00b8474/latest/USD').json()
    return response

class usdruViewSet(viewsets.ModelViewSet):
    queryset = usdru.objects.all().order_by('-json_from_api')
    serializer_class = usdruSerializer