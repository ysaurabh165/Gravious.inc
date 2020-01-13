from django.conf import settings
from django.db import models
from django.utils import timezone


class resident(models.Model):
	veh_id= models.CharField(max_length=20,primary_key=True)
	name = models.CharField(max_length=50)
	apartment = models.CharField(max_length=50)
	car_model= models.CharField(max_length=50)
	

	def publish(self):
		self.in_time = timezone.now()
		self.save()

	def __str__(self):
		return self.veh_id +str("             ")+self.name+str("             ")+self.apartment