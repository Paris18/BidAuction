from django.db import models


class default_columns(models.Model):
	Last_updated = models.DateTimeField(auto_now_add=True,blank = False)
	Created_on = models.DateTimeField(auto_now_add=True,blank = False)
	Valid = models.BooleanField(default=True)