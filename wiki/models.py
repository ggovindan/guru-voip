from django.db import models

# Create your models here.

class wikipage(models.Model):
	pagename=models.CharField(max_length=20, primary_key=True)
	content=models.TextField()

class ClientAddress(models.Model):
       userid=models.CharField(max_length=20, primary_key=True)
       currentAddress=models.CharField(max_length=100)
