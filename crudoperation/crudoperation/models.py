from django.db import models

class EmpModel(models.Model):
    patientname=models.CharField(max_length=100)
    gender=models.CharField(max_length=1)
    age=models.IntegerField()
    medicinename=models.CharField(max_length=100)
    empname=models.CharField(max_length=100)
    price=models.IntegerField()
    prescription_date=models.DateField()
    class Meta:
        db_table="prescription"