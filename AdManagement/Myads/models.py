from django.db import models
from .defaultColumns import default_columns

# Create your models here.


class adProperty(default_columns):
	Adid = models.CharField(max_length=10,primary_key=True)
	slot_Name = models.CharField(max_length=20)
	slot_from = models.DateTimeField(max_length=20)
	slot_to = models.DateTimeField(max_length=20)
	open_for_bid = models.BooleanField(default=True)
	min_bid_price = models.FloatField()

