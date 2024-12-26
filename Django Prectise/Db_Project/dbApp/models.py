from django.db import models

# Create your models here.
class EmployeeTab(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_Description=models.TextField()