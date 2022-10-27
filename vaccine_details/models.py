from django.db import models

# Create your models here.
class VaccineDetails(models.Model):
    list_id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=15)
    expire_date = models.DateField()
    availability = models.CharField(max_length=14)
    details = models.CharField(max_length=89)

    class Meta:
        managed = False
        db_table = 'vaccine_details'

