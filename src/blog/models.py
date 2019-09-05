from django.db import models

# Create your models here.
class Blog(models.Model):
	title		=models.CharField(max_length=120)
	description	=models.TextField()
	price		=models.TextField()
	summary		=models.TextField(default="this is cool!")