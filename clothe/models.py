from django.db import models

# Create your models here.
class Clothe(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.CharField(verbose_name='Description', max_length=255)
    brand = models.CharField(verbose_name='Brand', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg',upload_to='clothes/')

    class Meta:
        __tablename__ = 'Clothe'