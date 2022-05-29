# backend/notes/serializers.py
from rest_framework import serializers

from .models import usdru


class usdruSerializer(serializers.ModelSerializer):

    class Meta:
        model = usdru
        fields = ('id', 'current_date', 'date_from', 'date_to', 'json_from_api')