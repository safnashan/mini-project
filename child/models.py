from django.db import models
from parent.models import Parent
# Create your models here.
class Child(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    age = models.CharField(max_length=3)
    dob = models.DateField()
    vaccination_report = models.CharField(max_length=15)
    status = models.CharField(max_length=12)
    # p_id = models.IntegerField()
    p=models.ForeignKey(Parent,to_field='p_id', on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'child'

