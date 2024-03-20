from datetime import date
from django.db import models

# Create your models here.
class Payment(models.Model):
    user_id = models.IntegerField(db_column='user_id')
    order_id = models.IntegerField(db_column='order_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2, db_column='amount')
    method= models.CharField(max_length=255, db_column='method')
    date = models.DateTimeField(db_column='date')

    class Meta:
        db_table = 'payment'
    
    def __str__(self):
        return str(self.id)