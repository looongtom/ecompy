from django.db import models
from book.models import Book
 

# Create your models here.
class Cart(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(verbose_name='Quantity',default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    class Meta:
        __tablename__ = 'Cart' 
    
    def total(self):
        return self.quantity * self.book.price
    
    def name(self):
        return self.book.name
    
    def image(self):
        return self.book.image
    
    def price(self):
        return self.book.price

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

