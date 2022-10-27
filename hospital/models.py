from django.db import models

# Create your models here.
class Hospital(models.Model):
    h_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=15)
    contact_no = models.CharField(max_length=10)
    e_mail = models.CharField(max_length=13)
    since = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'hospital'

