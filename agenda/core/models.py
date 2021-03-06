from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_event = models.DateTimeField()
    date_create = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.title