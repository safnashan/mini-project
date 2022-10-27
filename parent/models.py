from django.db import models

# Create your models here.

class Parent(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    e_mail = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=15)
    address = models.CharField(max_length=25)
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'parent'
