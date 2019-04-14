from django.db import models
from Myads.defaultColumns import default_columns
from Myads.models import adProperty

# Create your models here.


class biddings(default_columns):
	Adid = models.ForeignKey(adProperty,on_delete=models.PROTECT)
	bid_price = models.FloatField()
	''' we Should use here ForienKey from bidder Service(not Created so directly using Name)'''
	bidder = models.CharField(max_length=20)

