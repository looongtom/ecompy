from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True)
    full_name = models.CharField(max_length=255, db_column='full_name')
    email = models.CharField(max_length=255, unique=True, db_column='email')
    password = models.CharField(max_length=255, db_column='password')
    phone = models.CharField(max_length=255, db_column='phone')
    address = models.CharField(max_length=255, db_column='address')
    role = models.CharField(max_length=30, db_column='role')

    class Meta:
        db_table = 'local_user'
        managed = True