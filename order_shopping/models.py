from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Order(models.Model):
    user_id = models.IntegerField(db_column='user_id')
    total = models.FloatField(db_column='total')
    date = models.DateTimeField(db_column='date')
    status = models.CharField(max_length=255, db_column='status')
    class Meta:
        db_table = 'order_shopping'

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order_id = models.IntegerField(db_column='order_id')
    cart= models.ForeignKey('cart.Cart', on_delete=models.CASCADE, null=True)
    