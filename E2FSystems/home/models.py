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

class UserSearch(models.Model):

    funding_stream = models.CharField(max_length=255)
    company_sector = models.CharField(max_length=255)
    estimated_annual_natural_gas_budget = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    employee_count = models.CharField(max_length=255)
    estimated_annual_electricity_budget = models.CharField(max_length=255)
    company_name = models.TextField(blank=True)
    company_contact = models.TextField(blank=True)

class ContactInfo(models.Model):
    contact_email = models.CharField(max_length=255)
    contact_company = models.CharField(max_length=255)
    additional_info = models.CharField(max_length=255, null=True, default=None)