from django.db import models
from parent.models import Parent
from child.models import Child

# Create your models here.
#
class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    vaccination_id = models.IntegerField()
    # p_id = models.IntegerField()
    p=models.ForeignKey(Parent,to_field='p_id', on_delete=models.CASCADE)
    status = models.CharField(max_length=12)
    doctor_name = models.CharField(max_length=56)
    # c_id = models.IntegerField()
    c = models.ForeignKey(Child, to_field='c_id', on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'booking'

