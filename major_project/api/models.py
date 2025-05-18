from django.db import models

class GlucoseReading(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    raw_data = models.JSONField() 
    glucose_level = models.FloatField()  # From ML model 
    timestamp = models.DateTimeField(auto_now_add=True)
