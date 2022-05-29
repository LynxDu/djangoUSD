# backend/notes/views.py
from rest_framework import viewsets

from .models import usdru
from .serializers import usdruSerializer


class usdruViewSet(viewsets.ModelViewSet):
    queryset = usdru.objects.all().order_by('-json_from_api')
    serializer_class = usdruSerializer