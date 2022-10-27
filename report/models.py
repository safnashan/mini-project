from django.db import models

# Create your models here.
class Report(models.Model):
    r_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    c_id = models.IntegerField()
    vaccination_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report'

