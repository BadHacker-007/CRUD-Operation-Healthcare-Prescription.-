from django.db import models
from django.contrib.sites.models import Site


class EmpModel(models.Model):
    patientname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    medicinename = models.CharField(max_length=100)
    empname = models.CharField(max_length=100)
    price = models.FloatField()
    prescription_date = models.DateField()
    patientpic = models.ImageField(upload_to='images/')
    history = models.BooleanField()
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        db_table = "prescription"
