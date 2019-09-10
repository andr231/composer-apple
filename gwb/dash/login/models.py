from django.db import models

class User(models.Model):
	usuario = models.CharField(max_length=300)
	nombre = models.CharField(max_length=300)
		
