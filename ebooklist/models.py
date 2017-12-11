import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class StoreId(models.Model):
    userid = models.CharField(max_length=20)
    aladin_id = models.CharField(max_length=20, blank=True, null=True)
    yes24_id = models.CharField(max_length=20, blank=True, null=True)
    ridibooks_id = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.userid
