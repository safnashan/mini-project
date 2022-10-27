from django.db import models

# Create your models here.

class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    list_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'slot'

