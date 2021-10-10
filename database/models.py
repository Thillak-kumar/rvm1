from django.db import models

# Create your models here.
class student(models.Model):
	Name = models.CharField(max_length=100)
	Roll_No= models.CharField(max_length=20)
	credits= models.CharField(max_length=20, db_column='No_of_days_present')
	credits_used= models.CharField(max_length=20, db_column='No_of_days_absent') 

