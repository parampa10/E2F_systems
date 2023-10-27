from django.db import models

# Create your models here.

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    project_type = models.CharField(max_length=500)
    supporting_docs=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    funding_stream=models.CharField(max_length=500)

class Admin(models.Model):
    
    username= models.CharField(max_length=100,primary_key=True)
    password= models.CharField(max_length=100)