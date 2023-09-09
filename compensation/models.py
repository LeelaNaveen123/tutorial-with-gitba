from django.db import models

# Create your models here.
class EmployeeCompensation(models.Model):
    '''Employee compensation class'''
    emp_identifier = models.FloatField()
    salary = models.FloatField()
    other_salary = models.FloatField()
    total_salary = models.FloatField()
    retirement = models.FloatField()
    health_dental = models.FloatField()
    other_benefits = models.FloatField()
    total_benefits = models.FloatField()
    total_compensation = models.FloatField()
    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now=True)
    


