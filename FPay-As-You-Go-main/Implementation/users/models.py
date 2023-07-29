from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
	

class Present(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	present=models.BooleanField(default=False)
	total_due = models.IntegerField(default=15)
	email=models.CharField(max_length=100)
	# user_id = models.IntegerField()
	paid = models.BooleanField(default=False)
	payment_name = models.CharField(max_length=50)
	pg_amt = models.IntegerField()
	
class Time(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	time=models.DateTimeField(null=True,blank=True)
	out=models.BooleanField(default=False)
	total_due = models.IntegerField(default=15)

class donate(models.Model):
	payment_name=models.CharField(max_length=50)
	# user=models.ForeignKey(User,on_delete=models.CASCADE)
	total_due = models.IntegerField( blank=True)
	email=models.CharField(max_length=100)
	# user_id = models.IntegerField()
	paid = models.BooleanField(default=False)