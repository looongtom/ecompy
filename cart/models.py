from django.db import models
from book.models import Book
from mobile.models import Mobile
from clothe.models import Clothe
# Create your models here.
class Cart(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(verbose_name='Quantity',default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    mobile= models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True)
    clothe= models.ForeignKey(Clothe, on_delete=models.CASCADE, null=True)
    status= models.CharField(verbose_name='Status', max_length=255, default='available')

    class Meta:
        __tablename__ = 'Cart' 
    
    def total(self):
        if self.book:
            return self.quantity * self.book.price
        elif self.mobile:
            return self.quantity * self.mobile.price
        elif self.clothe:
            return self.quantity * self.clothe.price
    
    def name(self):
        if self.book:
            return self.book.name
        elif self.mobile:
            return self.mobile.name
        elif self.clothe:
            return self.clothe.name
    
    def image(self):
        if self.book:
            return self.book.image
        elif self.mobile:
            return self.mobile.image
        elif self.clothe:
            return self.clothe.image
    
    def price(self):
        if self.book:
            return self.book.price
        elif self.mobile:
            return self.mobile.price
        elif self.clothe:
            return self.clothe.price

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

