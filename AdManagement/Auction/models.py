from django.db import models
from biddings.models import biddings
from Myads.models import adProperty

# Create your models here.

class WinnerBid(models.Model):
	Adid = models.ForeignKey(adProperty,on_delete=models.PROTECT)
	bidid = models.ForeignKey(biddings,on_delete=models.PROTECT)

