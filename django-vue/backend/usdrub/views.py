# backend/notes/views.py
from rest_framework import viewsets

from .models import usdru
from .serializers import usdruSerializer

import requests
import json


class usdruViewSet(viewsets.ModelViewSet):

    url = 'https://v6.exchangerate-api.com/v6/632cda93e818793dd00b8474/latest/USD'

    # Making our request
    response = requests.get(url)
    data = response.json()
    data1 = json.dumps(data)
    queryset = usdru.objects.create(current_date=data['conversion_rates']['RUB'], date_from=data['time_last_update_utc'], date_to=data['time_next_update_utc'], json_from_api=data1)
    # ('id', 'current_date', 'date_from', 'date_to', 'json_from_api')
    queryset.save()
    queryset = usdru.objects.all().order_by('-json_from_api')
    serializer_class = usdruSerializer
