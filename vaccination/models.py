from django.db import models

# Create your models here.
class Vaccination(models.Model):
    vaccination_id = models.AutoField(primary_key=True)
    list_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    age_category = models.CharField(max_length=12)
    status = models.CharField(max_length=45)
    p_id = models.IntegerField()
    c_id = models.IntegerField()


class Meta:
        managed = False
        db_table = 'vaccination'

