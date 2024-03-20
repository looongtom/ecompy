from django.db import models

# Create your models here.
class Shipment(models.Model):
    user_id = models.IntegerField(db_column='user_id')
    order_id = models.IntegerField(db_column='order_id')
    address = models.CharField(max_length=255, db_column='address')
    date = models.DateTimeField(db_column='date')
    status = models.CharField(max_length=255, db_column='status')
    class Meta:
        db_table = 'shipment'
    
    def __str__(self):
        return str(self.id)