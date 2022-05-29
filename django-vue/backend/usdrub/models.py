from django.db import models
class usdru(models.Model):

    current_date = models.FloatField()
    date_from = models.DateTimeField(auto_now_add=True)
    date_to = models.DateTimeField(auto_now_add=True)
    json_from_api = models.CharField(max_length=255)